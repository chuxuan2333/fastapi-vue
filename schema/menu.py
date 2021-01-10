from pydantic import BaseModel
from typing import Optional


class MenuBase(BaseModel):
    menu_name: str
    menu_flag: str
    parent_id: str = '0'
    menu_id: Optional[str] = ''
