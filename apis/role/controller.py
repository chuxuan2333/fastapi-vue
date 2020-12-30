from fastapi import APIRouter, Depends, HTTPException
from core.db import get_session
from sqlalchemy.orm import Session
from models.role.models import Role, RoleUserRelation
from models.user.models import User
from schema.role import RoleList, RoleBase, RoleAddUsers, RoleUsers

role_router = APIRouter()


@role_router.get("/list", response_model=RoleList, name="获取角色列表")
async def role_list(db: Session = Depends(get_session)):
    roles = db.query(Role).all()
    role_lists = {"roles": [RoleBase(**{"role_name": role.role_name, "role_desc": role.role_desc}) for role in roles]}
    return role_lists


@role_router.put("/add_role", name="新增角色")
async def add_role(role: RoleBase, db: Session = Depends(get_session)):
    old_role = db.query(Role).filter(Role.role_name == role.role_name).first()
    if old_role:
        return HTTPException(status_code=406, detail="创建的角色已存在")
    new_role = Role(**role.dict())
    db.add(new_role)
    db.commit()
    return {"message": "角色添加成功"}


@role_router.post("/add_users", name="新增成员")
async def role_add_user(role_users: RoleAddUsers, db: Session = Depends(get_session)):
    role_id = int(role_users.role_id)
    # 判断role是否存在
    role = db.query(Role.role_id == role_id).first()
    if not role:
        return HTTPException(status_code=406, detail="角色不存在")
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

    return {"message": "成员添加成功"}


@role_router.get("/user_lists", response_model=RoleUsers, name="角色下所有成员")
async def role_user_lists(role_id: str, db: Session = Depends(get_session)):
    # 通过role去查询所有用户
    users = db.query(User.user_id, User.username).join(RoleUserRelation,
                                                       RoleUserRelation.user_id == User.user_id).filter(
        RoleUserRelation.role_id == int(role_id)).all()
    role_users = [{"user_id": str(user.user_id), "username": user.username} for user in users]
    return RoleUsers(users=role_users)
