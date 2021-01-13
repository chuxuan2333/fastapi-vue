from fastapi import APIRouter, Depends, HTTPException, Request
from schema.cmdb import CMDBTypeList, CMDBBase
from models.cmdb.models import CMDBType
from models.user.models import User
from core.db import get_db
from apis.perm.controller import check_perm
from sqlalchemy.orm import Session
from utils.Record import Record
from copy import deepcopy

cmdb_router = APIRouter()


@cmdb_router.get('/type_list', response_model=CMDBTypeList, name="获取CMDB中所有对象类型")
def cmdb_type_list(db: Session = Depends(get_db), current_user: User = Depends(check_perm('/cmdb/type_list'))):
    cmdb_types = db.query(CMDBType).all()
    return CMDBTypeList(types=[{"type_id": str(cmdb_type.cmdb_type_id), "type_name": cmdb_type.cmdb_type_name,
                                "type_label": cmdb_type.cmdb_type_label, "type_icon": cmdb_type.cmdb_type_icon} for
                               cmdb_type in cmdb_types])


@cmdb_router.put('/add_type', name="新增CMDB对象类型")
def cmdb_add_type(new_type: CMDBBase, request: Request, db: Session = Depends(get_db),
                  current_user: User = Depends(check_perm('/cmdb/add_type'))):
    # type_name唯一
    old_type = db.query(CMDBType).filter(CMDBType.cmdb_type_name == new_type.type_name).first()
    if old_type:
        raise HTTPException(status_code=406, detail="创建的类型已经存在")
    cmdb_type = CMDBType(cmdb_type_name=new_type.type_name, cmdb_type_icon=new_type.type_icon,
                         cmdb_type_label=new_type.type_label)
    new_record = deepcopy(cmdb_type)
    db.add(cmdb_type)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_record, ip=request.client.host)
    return {"message": "类型创建成功"}


@cmdb_router.post('/edit_type', name="修改CMDB对象类型")
def cmdb_edit_type(edit_type: CMDBBase, request: Request, db: Session = Depends(get_db),
                   current_user: User = Depends(check_perm('/cmdb/edit_type'))):
    old_type = db.query(CMDBType.cmdb_type_id == int(edit_type.type_id)).first()
    if not old_type:
        raise HTTPException(status_code=406, detail="要修改的类型不存在")
    if old_type.cmdb_type_name != edit_type.type_name:
        # 说明修改了类型名，需要判断修改后的类型是否已经存在
        old_type = db.query(CMDBType.cmdb_type_name == edit_type.type_name).first()
        if old_type:
            raise HTTPException(status_code=406, detail="修改的类型已存在")
    old_record = deepcopy(old_type)
    old_type.cmdb_type_name = edit_type.type_name
    old_type.cmdb_type_icon = edit_type.type_icon
    old_type.cmdb_type_label = edit_type.type_label
    new_record = deepcopy(old_type)
    db.add(old_type)
    db.commit()
    Record.create_operate_record(username=current_user.username, old_object=old_record, new_object=new_record,
                                 ip=request.client.host)
    return {"message": "类型修改成功"}
