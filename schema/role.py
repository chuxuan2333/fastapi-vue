from pydantic import BaseModel
from typing import List


class RoleBase(BaseModel):
    role_name: str
    role_desc: str


class RoleList(BaseModel):
    roles: List[RoleBase] = []


class RoleAddUsers(BaseModel):
    # 添加成员模型
    role_id: str
    users: List[str]


class RoleUser(BaseModel):
    # 查询成员模型
    user_id: str
    username: str


class RoleUsers(BaseModel):
    users: List[RoleUser]
