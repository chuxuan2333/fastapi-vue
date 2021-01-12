from copy import deepcopy
from fastapi import APIRouter, Depends, HTTPException, Request
from core.db import get_db
from models.user.models import User
from models.role.models import RoleUserRelation, MenuRoleRelation
from models.menu.models import Menu
from apis.perm.controller import check_perm
from apis.login.controller import get_current_active_user
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from schema.user import UserBase, NewUser, AllUser, ModifyUser
from utils.Record import Record

user_router = APIRouter()


@user_router.get("/me", response_model=UserBase, name="获取登陆用户详情")
async def me(user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    menus = db.query(Menu.menu_flag).join(MenuRoleRelation, MenuRoleRelation.menu_id == Menu.menu_id).join(
        RoleUserRelation, RoleUserRelation.role_id == MenuRoleRelation.role_id).filter(
        RoleUserRelation.user_id == user.user_id).all()
    menus = [menu.menu_flag for menu in menus]
    user_dict = {"username": user.username, "email": user.email, "is_active": user.is_active,
                 "nick_name": user.nick_name,
                 "menus": menus}
    return UserBase(**user_dict)


@user_router.get("/get_user_info", response_model=UserBase, name="获取指定用户详情")
async def get_user_info(username: str, db: Session = Depends(get_db),
                  current_user: User = Depends(check_perm('/users/get_user_info'))):
    user = db.query(User).filter(User.username == username).first()
    if user:
        user_dict = {"username": user.username, "email": user.email, "is_active": user.is_active,
                     "nick_name": user.nick_name}
        return UserBase(**user_dict)
    else:
        raise HTTPException(status_code=406, detail="用户不存在")


@user_router.get("/all_users", response_model=AllUser, name="获取所有用户")
async def all_users(page_no: int, page_size: int, search_username: str = '', db: Session = Depends(get_db),
              current_user: User = Depends(check_perm('/users/all_users'))):
    # 分页查询,前端需要传递页数,和每页多少个
    # 数据分页与list切片格式保持一致
    if search_username:
        total = db.query(func.count(User.user_id)).filter(User.username == search_username).scalar()
        users = db.query(User).filter(User.username == search_username).slice(page_size * (page_no - 1),
                                                                              page_size * page_no)
    else:
        total = db.query(func.count(User.user_id)).scalar()
        users = db.query(User).slice(page_size * (page_no - 1), page_size * page_no)
    all_users_dict = {"total": total, "users": [UserBase(
        **{"username": user.username, "email": user.email, "is_active": user.is_active, "nick_name": user.nick_name})
        for user in users]}
    return AllUser(**all_users_dict)


@user_router.put("/create_user", responses={406: {"description": "创建的用户已经存在"}}, name="创建新用户")
async def create_user(user: NewUser, request: Request, db: Session = Depends(get_db),
                current_user: User = Depends(check_perm('/users/create_user'))):
    old_user = db.query(User).filter(or_(User.username == user.username, User.email == user.email)).first()
    if old_user:
        raise HTTPException(status_code=406, detail="创建的用户已经存在")
    user_dict = {"username": user.username, "email": user.email, "nick_name": user.nick_name,
                 "is_active": user.is_active}
    new_user = User(**user_dict)
    new_record = deepcopy(new_user)
    new_user.convert_pass_to_hash(user.password)
    db.add(new_user)
    db.commit()
    # 调用数据修改记录器
    Record.create_operate_record(new_object=new_record, username=current_user.username, ip=request.client.host)
    return {"message": "用户创建成功"}


@user_router.post("/update_user", name="更新用户信息")
async def update_user(request: Request, modify_user: ModifyUser, db: Session = Depends(get_db),
                current_user: User = Depends(check_perm('/users/update_user'))):
    """
    用户名不可以修改
    """
    user = db.query(User).filter(User.username == modify_user.username).first()
    if user:
        old_user = deepcopy(user)
        if modify_user.password:
            user.convert_pass_to_hash(modify_user.password)
        user.is_active = modify_user.is_active
        user.email = modify_user.email
        user.nick_name = modify_user.nick_name
        new_user = deepcopy(user)
        db.add(user)
        db.commit()
        # 调用数据修改记录器
        Record.create_operate_record(old_object=old_user, new_object=new_user, username=current_user.username,
                                     ip=request.client.host)
        return {"message": "用户信息更新成功"}
    else:
        raise HTTPException(status_code=406, detail="用户不存在")
