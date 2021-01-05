from fastapi import APIRouter, Depends, HTTPException, Request
from core.db import get_session
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.role.models import Role, RoleUserRelation, PermRoleRelation
from models.user.models import User
from models.perm.models import Permission
from apis.perm.controller import check_perm
from utils.Record import Record
from schema.role import RoleList, RoleBase, RoleEditUsers, RoleUsers, RolePerms, RoleEditPerms

role_router = APIRouter()


@role_router.get("/list", response_model=RoleList, name="角色列表")
async def role_list(db: Session = Depends(get_session), current_user: User = Depends(check_perm('/role/list'))):
    roles = db.query(Role, func.count(RoleUserRelation.user_id).label('user_count')).outerjoin(
        RoleUserRelation,
        RoleUserRelation.role_id == Role.role_id).group_by(Role.role_name).all()
    role_lists = {"roles": [
        RoleBase(**{"role_name": role.Role.role_name, "role_desc": role.Role.role_desc, "role_id": role.Role.role_id,
                    "user_count": role.user_count}) for role in roles]}
    return role_lists


@role_router.put("/add_role", name="新增角色")
async def add_role(role: RoleBase, request: Request, db: Session = Depends(get_session),
                   current_user: User = Depends(check_perm('/role/add_role'))):
    old_role = db.query(Role).filter(Role.role_name == role.role_name).first()
    if old_role:
        raise HTTPException(status_code=406, detail="创建的角色已存在")
    new_role = Role(role_name=role.role_name, role_desc=role.role_desc)
    db.add(new_role)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_role, ip=request.client.host)
    return {"message": "角色添加成功"}


@role_router.post("/edit_users", name="角色成员修改")
async def role_edit_user(role_users: RoleEditUsers, db: Session = Depends(get_session),
                         current_user: User = Depends(check_perm('/role/edit_users'))):
    role_id = int(role_users.role_id)
    # 判断role是否存在
    role = db.query(Role.role_id == role_id).first()
    if not role:
        raise HTTPException(status_code=406, detail="角色不存在")
    # todo 此处是否要判断user_id是否正确？
    # 处理关联表
    # 清除所有数据
    db.query(RoleUserRelation).filter(RoleUserRelation.role_id == role_id).delete()
    for user_id in role_users.users:
        user_id = int(user_id)
        db.query(RoleUserRelation).filter(RoleUserRelation.user_id == user_id).delete()
        role_user_relation = RoleUserRelation(**{"role_id": role_id, "user_id": user_id})
        db.add(role_user_relation)
        db.commit()

    return {"message": "成员修改成功"}


@role_router.post("/edit_perms", name="角色权限修改")
def role_edit_perms(edit_perms: RoleEditPerms, db: Session = Depends(get_session),
                    current_user: User = Depends(check_perm('/role/edit_perms'))):
    role_id = int(edit_perms.role_id)
    # 判断role是否存在
    role = db.query(Role.role_id == role_id).first()
    if not role:
        raise HTTPException(status_code=406, detail="角色不存在")
    # 处理关联表
    # 清除所有数据
    db.query(PermRoleRelation).filter(PermRoleRelation.role_id == role_id).delete()
    for perm_id in edit_perms.perms:
        perm_id = int(perm_id)
        role_perm_relation = PermRoleRelation(**{"role_id": role_id, "perm_id": perm_id})
        db.add(role_perm_relation)
        db.commit()
    return {"message": "权限修改成功"}


@role_router.get("/user_lists", response_model=RoleUsers, name="角色下所有成员")
async def role_user_lists(role_id: str, db: Session = Depends(get_session),
                          current_user: User = Depends(check_perm('/role/user_lists'))):
    # 通过role去查询所有用户
    users = db.query(User.user_id).join(RoleUserRelation, RoleUserRelation.user_id == User.user_id).filter(
        RoleUserRelation.role_id == int(role_id)).all()
    all_users = db.query(User).all()
    role_users = [{"key": str(user.user_id), "label": user.username} for user in all_users]
    return RoleUsers(users=role_users, choose_users=[str(member.user_id) for member in users])


@role_router.get("/perm_lists", response_model=RolePerms, name="角色下所有权限")
async def perm_lists(role_id: str, db: Session = Depends(get_session),
                     current_user: User = Depends(check_perm('/role/perm_lists'))):
    # 通过role查询权限
    perms = db.query(Permission.perm_id).join(PermRoleRelation, PermRoleRelation.perm_id == Permission.perm_id).filter(
        PermRoleRelation.role_id == int(role_id)).all()
    all_perms = db.query(Permission).all()
    role_perms = [{"key": str(perm.perm_id), "label": perm.perm_name} for perm in all_perms]
    return RolePerms(perms=role_perms, choose_perms=[str(perm.perm_id) for perm in perms])
