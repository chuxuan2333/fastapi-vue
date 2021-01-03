from pydantic import BaseModel
from typing import List, Optional


class RoleBase(BaseModel):
    role_id: Optional[str] = None
    role_name: str
    role_desc: str
    user_count: Optional[int] = None


class RoleList(BaseModel):
    roles: List[RoleBase] = []


class RoleAddUsers(BaseModel):
    # 添加成员模型
    role_id: str
    users: List[str]


class RoleUser(BaseModel):
    # 查询成员模型
    key: str
    label: str


class RoleUsers(BaseModel):
    # 所有用户
    users: List[RoleUser]
    # role下面的用户id list
    choose_users: List[str]
