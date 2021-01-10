from pydantic import BaseModel
from typing import List, Optional


class RoleBase(BaseModel):
    role_id: Optional[str] = None
    role_name: str
    role_desc: str
    user_count: Optional[int] = None


class RoleList(BaseModel):
    roles: List[RoleBase] = []


class RoleEditUsers(BaseModel):
    # 修改成员模型
    role_id: str
    users: List[str]


class RoleEditBase(BaseModel):
    # 查询成员模型
    key: str
    label: str


class RoleUsers(BaseModel):
    # 所有用户
    users: List[RoleEditBase]
    # role下面的用户id list
    choose_users: List[str]


class PermBase(BaseModel):
    # 权限基础模型
    perm_id: Optional[str] = None
    perm_name: str
    perm_interface: str


class PermList(BaseModel):
    # 权限列表
    total: int
    perms: List[PermBase]


class RolePerms(BaseModel):
    perms: List[RoleEditBase]
    choose_perms: List[str]


class RoleMenus(BaseModel):
    menus: List[RoleEditBase]
    choose_menus: List[str]


class RoleEditPerms(BaseModel):
    # 修改权限模型
    role_id: str
    perms: List[str]


class RoleEditMenus(BaseModel):
    role_id: str
    menus: List[str]
