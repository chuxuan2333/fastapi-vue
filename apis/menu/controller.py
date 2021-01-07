from fastapi import APIRouter, Depends
from models.menu.models import Menu
from sqlalchemy.orm import Session
from core.db import get_session
import json
menu_router = APIRouter()


@menu_router.get('/menu_lists', name="菜单列表")
def menu_lists(db: Session = Depends(get_session)):
    # 查询一级菜单
    menu_list = []
    all_menus = db.query(Menu).all()
    parent_menus = db.query(Menu).filter(Menu.parent_id == 0).all()
    all_parent_ids = [menu.parent_id for menu in db.query(Menu.parent_id).distinct().all()]
    for parent_menu in parent_menus:
        # 递归获得子菜单
        parent_menu_dict = {"menu_id": parent_menu.menu_id, "menu_name": parent_menu.menu_name}
        if parent_menu.menu_id in all_parent_ids:
            parent_menu_dict["children"] = get_menus(parent_menu.menu_id, all_menus, all_parent_ids)
        menu_list.append(parent_menu_dict)
    print(json.dumps(menu_list))


def get_menus(parent_id, all_menus, all_parent_ids):
    child_menus = []
    child_menus_dicts = []
    for menu in all_menus:
        if menu.parent_id == parent_id:
            child_menus.append(menu)
    for child_menu in child_menus:
        # 判断有没有子菜单
        child_menus_dict = {"menu_id": child_menu.menu_id, "menu_name": child_menu.menu_name}
        if child_menu.menu_id in all_parent_ids:
            child_menus_dict["children"] = get_menus(child_menu.menu_id, all_menus, all_parent_ids)
        child_menus_dicts.append(child_menus_dict)
    if len(child_menus) == 0:
        return
    return child_menus_dicts
