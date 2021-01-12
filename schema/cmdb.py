from pydantic import BaseModel
from typing import List, Optional


class CMDBBase(BaseModel):
    type_id: Optional[str] = None
    type_name: str
    type_icon: str


class CMDBTypeList(BaseModel):
    types: List[CMDBBase]
