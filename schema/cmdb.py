from pydantic import BaseModel
from typing import List, Optional


class CMDBBase(BaseModel):
    type_id: Optional[str] = None
    type_name: str
    type_label: str
    type_icon: str


class CMDBTypeList(BaseModel):
    types: List[CMDBBase]


class CMDBItemBase(BaseModel):
    item_id: Optional[str] = None
    cmdb_type_id: Optional[str] = None
    item_label: str
    item_name: str


class CMDBItemList(BaseModel):
    items: List[CMDBItemBase]


class ServerInfo(BaseModel):
    ip: str
    username: str
    port: str
    password: str
