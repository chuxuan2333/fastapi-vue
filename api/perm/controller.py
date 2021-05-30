from fastapi import APIRouter, Depends, HTTPException, Request
from models.perm.models import Permission
from models.role.models import RoleUserRelation, PermRoleRelation
from models.user.models import User
from core.db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from schema.role import PermList, PermBase
from api.login.controller import get_current_active_user
from utils.Record import Record
from core.config import settings
from copy import deepcopy

perm_router = APIRouter()


def check_perm(interface: str):
    """
    验证用户是否有对应接口权限
    """

    def check_user_permission(current_user: User = Depends(get_current_active_user),
                              db: Session = Depends(get_db)):
        # 查询拥有权限的user
        users = db.query(RoleUserRelation.user_id).join(PermRoleRelation,
                                                        PermRoleRelation.role_id == RoleUserRelation.role_id).join(
            Permission, Permission.perm_id == PermRoleRelation.perm_id).filter(
            Permission.perm_interface == interface).all()
        user_ids = [user.user_id for user in users]
        if current_user.user_id in user_ids:
            return current_user
        else:
            settings.logger.info(f"{current_user.username}没有分配{interface}权限")
            raise HTTPException(status_code=406, detail="没有权限")

    return check_user_permission


@perm_router.get('/perm_lists', response_model=PermList, name="权限列表")
async def perm_lists(page_no: int, page_size: int, search_perm: str = '', db: Session = Depends(get_db),
                     user: User = Depends(check_perm('/perm/perm_lists'))):
    if search_perm:
        total = db.query(func.count(Permission.perm_id)).filter(or_(Permission.perm_name.like(f"%{search_perm}%"),
                                                                    Permission.perm_interface.like(
                                                                        f"%{search_perm}%"))).scalar()
        perms = db.query(Permission).filter(or_(Permission.perm_name.like(f"%{search_perm}%"),
                                                Permission.perm_interface.like(f"%{search_perm}%"))).slice(
            page_size * (page_no - 1), page_size * page_no)
    else:
        total = db.query(func.count(Permission.perm_id)).scalar()
        perms = db.query(Permission).slice(page_size * (page_no - 1), page_size * page_no)
    perm_list = {"total": total,
                 "perms": [{"perm_id": perm.perm_id, "perm_name": perm.perm_name, "perm_interface": perm.perm_interface}
                           for perm in perms]}

    return PermList(**perm_list)


@perm_router.put('/add_perm', name="新增权限")
async def add_perm(new_perm: PermBase, request: Request, db: Session = Depends(get_db),
                   current_user: User = Depends(check_perm('/perm/add_perm'))):
    # 查询是否存在
    old_perm = db.query(Permission).filter(
        or_(Permission.perm_name == new_perm.perm_name, Permission.perm_interface == new_perm.perm_interface)).first()
    if old_perm:
        raise HTTPException(status_code=406, detail="权限已存在")
    perm = Permission(perm_name=new_perm.perm_name, perm_interface=new_perm.perm_interface)
    new_record = deepcopy(perm)
    db.add(perm)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_record, ip=request.client.host)
    return {"message": "权限已添加"}


@perm_router.post('/edit_perm/{perm_id}', name="修改权限")
async def edit_perm(perm_id: str, perm_edit: PermBase, request: Request, db: Session = Depends(get_db),
                    current_user: User = Depends(check_perm("/perm/edit_perm"))):
    # 查询
    perm = db.query(Permission).filter(Permission.perm_id == int(perm_id)).first()
    if not perm:
        raise HTTPException(status_code=406, detail="需要修改的权限不存在")
    # 判断是否重复
    if perm_edit.perm_name != perm.perm_name:
        old_perm = db.query(Permission).filter(Permission.perm_name == perm_edit.perm_name).first()
        if old_perm:
            raise HTTPException(status_code=406, detail="修改后的权限名称重复")
    if perm_edit.perm_interface != perm.perm_interface:
        old_perm = db.query(Permission).filter(Permission.perm_interface == perm_edit.perm_interface).first()
        if old_perm:
            raise HTTPException(status_code=406, detail="修改后的权限接口重复")
    old_perm = deepcopy(perm)
    perm.perm_name = perm_edit.perm_name
    perm.perm_interface = perm_edit.perm_interface
    new_perm = deepcopy(perm)
    db.add(perm)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_perm, old_object=old_perm,
                                 ip=request.client.host)
    return {"message": "权限修改成功"}
