from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from models.menu.models import Menu
from sqlalchemy.orm import Session
from sqlalchemy import or_
from core.db import get_db
from api.perm.controller import check_perm
from models.user.models import User
from schema.menu import MenuBase
from copy import deepcopy
from utils.Record import Record
from core.config import settings

menu_router = APIRouter()


@menu_router.get('/menu_lists', name="菜单列表")
async def menu_lists(db: Session = Depends(get_db), current_user: User = Depends(check_perm('/menu/menu_lists'))):
    # 查询一级菜单
    menu_list = []
    all_menus = db.query(Menu).all()
    parent_menus = db.query(Menu).filter(Menu.parent_id == 0).all()
    all_parent_ids = [menu.parent_id for menu in db.query(Menu.parent_id).distinct().all()]
    for parent_menu in parent_menus:
        # 递归获得子菜单
        parent_menu_dict = {"menu_id": str(parent_menu.menu_id), "menu_name": parent_menu.menu_name}
        if parent_menu.menu_id in all_parent_ids:
            parent_menu_dict["children"] = get_menus(parent_menu.menu_id, all_menus, all_parent_ids)
        menu_list.append(parent_menu_dict)
    return JSONResponse({"menus": menu_list})


@menu_router.put('/add_menu', name="新增菜单")
async def add_menu(menu: MenuBase, request: Request, db: Session = Depends(get_db),
                   current_user: User = Depends(check_perm('/menu/add_menu'))):
    # 确认menu不存在
    old_menu = db.query(Menu).filter(or_(Menu.menu_name == menu.menu_name, Menu.menu_flag == menu.menu_flag)).first()
    if old_menu:
        raise HTTPException(status_code=406, detail="菜单已存在")
    new_menu = Menu(menu_name=menu.menu_name, menu_flag=menu.menu_flag,
                    parent_id="0" if not menu.parent_id else int(menu.parent_id))
    new_record = deepcopy(new_menu)
    db.add(new_menu)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_record, ip=request.client.host)
    settings.logger.info(f"新增菜单{menu.menu_name}")
    return {"message": "菜单新增成功"}


@menu_router.post('/edit_menu', name="修改菜单")
async def edit_menu(menu: MenuBase, request: Request, db: Session = Depends(get_db),
                    current_user: User = Depends(check_perm('/menu/edit_menu'))):
    # 确认menu不存在
    old_menu = db.query(Menu).filter(Menu.menu_id == int(menu.menu_id)).first()
    if not old_menu:
        raise HTTPException(status_code=406, detail="要修改的菜单不存在")
    # 确认菜单是否重复
    old_record = deepcopy(old_menu)
    if menu.menu_name != old_menu.menu_name:
        if db.query(Menu).filter(Menu.menu_name == menu.menu_name).first():
            raise HTTPException(status_code=406, detail="菜单名已存在")
    if menu.menu_flag != old_menu.menu_flag:
        if db.query(Menu).filter(Menu.menu_flag == menu.menu_flag).first():
            raise HTTPException(status_code=406, detail="菜单标识已存在")
    old_menu.menu_name = menu.menu_name
    old_menu.menu_flag = menu.menu_flag
    old_menu.parent_id = int(menu.parent_id)
    new_record = deepcopy(old_menu)
    db.add(old_menu)
    db.commit()
    Record.create_operate_record(username=current_user.username, old_object=old_record, new_object=new_record,
                                 ip=request.client.host)
    return {"message": "菜单修改成功"}


@menu_router.get('/get_menu_info', name="获取菜单详细信息")
async def get_menu_info(menu_id: str, db: Session = Depends(get_db),
                        current_user: User = Depends(check_perm('/menu/get_menu_info'))):
    menu = db.query(Menu).filter(Menu.menu_id == int(menu_id)).first()
    if not menu:
        raise HTTPException(status_code=406, detail="没有此菜单")
    return MenuBase(menu_id=menu_id, menu_name=menu.menu_name, menu_flag=menu.menu_flag, parent_id=str(menu.parent_id))


def get_menus(parent_id, all_menus, all_parent_ids):
    child_menus = []
    child_menus_dicts = []
    for menu in all_menus:
        if menu.parent_id == parent_id:
            child_menus.append(menu)
    for child_menu in child_menus:
        # 判断有没有子菜单
        child_menus_dict = {"menu_id": str(child_menu.menu_id), "menu_name": child_menu.menu_name}
        if child_menu.menu_id in all_parent_ids:
            child_menus_dict["children"] = get_menus(child_menu.menu_id, all_menus, all_parent_ids)
        child_menus_dicts.append(child_menus_dict)
    if len(child_menus) == 0:
        return
    return child_menus_dicts
