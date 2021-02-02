from fastapi import APIRouter, Depends, HTTPException, Request, WebSocket, status
from schema.cmdb import CMDBTypeList, CMDBBase, CMDBItemBase, CMDBItemList
from models.cmdb.models import CMDBType, CMDBItem, CMDBRecord
from models.user.models import User
from core.db import get_db
from apis.perm.controller import check_perm
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from utils.Record import Record
from copy import deepcopy
from typing import Dict
import paramiko
from threading import Thread
import asyncio

cmdb_router = APIRouter()


@cmdb_router.get('/type_list', response_model=CMDBTypeList, name="获取CMDB中所有对象类型")
async def cmdb_type_list(db: Session = Depends(get_db), current_user: User = Depends(check_perm('/cmdb/type_list'))):
    cmdb_types = db.query(CMDBType).all()
    return CMDBTypeList(types=[{"type_id": str(cmdb_type.cmdb_type_id), "type_name": cmdb_type.cmdb_type_name,
                                "type_label": cmdb_type.cmdb_type_label, "type_icon": cmdb_type.cmdb_type_icon} for
                               cmdb_type in cmdb_types])


@cmdb_router.put('/add_type', name="新增CMDB对象类型")
async def cmdb_add_type(new_type: CMDBBase, request: Request, db: Session = Depends(get_db),
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


@cmdb_router.get('/type_info', name="获取CMDB对象属性")
async def type_info(type_id: str, db: Session = Depends(get_db),
                    current_user: User = Depends(check_perm('/cmdb/type_info'))):
    search_type = db.query(CMDBType).filter(CMDBType.cmdb_type_id == int(type_id)).first()
    if not search_type:
        raise HTTPException(status_code=406, detail="查询ID不存在")
    return CMDBBase(type_id=type_id, type_name=search_type.cmdb_type_name, type_label=search_type.cmdb_type_label,
                    type_icon=search_type.cmdb_type_icon)


@cmdb_router.post('/edit_type', name="修改CMDB对象类型")
async def cmdb_edit_type(edit_type: CMDBBase, request: Request, db: Session = Depends(get_db),
                         current_user: User = Depends(check_perm('/cmdb/edit_type'))):
    old_type = db.query(CMDBType).filter(CMDBType.cmdb_type_id == int(edit_type.type_id)).first()
    if not old_type:
        raise HTTPException(status_code=406, detail="要修改的类型不存在")
    if old_type.cmdb_type_name != edit_type.type_name:
        # 说明修改了类型名，需要判断修改后的类型是否已经存在
        if db.query(CMDBType).filter(CMDBType.cmdb_type_name == edit_type.type_name).first():
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


@cmdb_router.get('/get_type_items', name="获取类型下所有的属性")
async def get_type_desc(type_id: str, db: Session = Depends(get_db),
                        current_user: User = Depends(check_perm('/cmdb/get_type_items'))):
    cmdb_type_items = db.query(CMDBItem).filter(CMDBItem.cmdb_type_id == int(type_id)).all()
    return CMDBItemList(items=[{"item_id": cmdb_type_item.item_id, "item_label": cmdb_type_item.item_label,
                                "item_name": cmdb_type_item.item_name} for cmdb_type_item in cmdb_type_items])


@cmdb_router.put('/add_type_item', name="新增类型属性")
async def add_type_desc(request: Request, new_item: CMDBItemBase, db: Session = Depends(get_db),
                        current_user: User = Depends(check_perm('/cmdb/add_type_item'))):
    # 确认属性是否重复
    old_item = db.query(CMDBItem).filter(and_(CMDBItem.cmdb_type_id == new_item.cmdb_type_id,
                                              or_(CMDBItem.item_name == new_item.item_name,
                                                  CMDBItem.item_label == new_item.item_label))).first()
    if old_item:
        raise HTTPException(status_code=406, detail="此属性已存在")
    item = CMDBItem(cmdb_type_id=int(new_item.cmdb_type_id), item_name=new_item.item_name,
                    item_label=new_item.item_label)
    new_record = deepcopy(item)
    db.add(item)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_record, ip=request.client.host)
    return {"message": "属性新增成功"}


@cmdb_router.get('/item_info', name="获取类型属性详情")
def item_info(item_id: str, db: Session = Depends(get_db), current_user: User = Depends(check_perm('/cmdb/item_info'))):
    item = db.query(CMDBItem).filter(CMDBItem.item_id == int(item_id)).first()
    if not item:
        raise HTTPException(status_code=406, detail="查询ID不存在")
    return CMDBItemBase(item_id=item_id, cmdb_type_id=str(item.cmdb_type_id), item_label=item.item_label,
                        item_name=item.item_name)


@cmdb_router.post('/edit_type_item', name="修改类型属性")
async def edit_type_item(request: Request, edit_item: CMDBItemBase, db: Session = Depends(get_db),
                         current_user: User = Depends(check_perm('/cmdb/edit_type_item'))):
    type_id = int(edit_item.item_id)
    old_item = db.query(CMDBItem).filter(CMDBItem.item_id == type_id).first()
    if not old_item:
        raise HTTPException(status_code=406, detail="要修改的属性不存在")
    # 判断是否存在
    if old_item.item_name != edit_item.item_name:
        if db.query(CMDBItem).filter(and_(CMDBItem.cmdb_type_id == int(edit_item.cmdb_type_id),
                                          CMDBItem.item_name == edit_item.item_name)).first():
            raise HTTPException(status_code=406, detail="要修改的属性名已存在")
    if old_item.item_label != edit_item.item_label:
        if db.query(CMDBItem).filter(and_(CMDBItem.cmdb_type_id == int(edit_item.cmdb_type_id),
                                          CMDBItem.item_label == edit_item.item_label)).first():
            raise HTTPException(status_code=406, detail="要修改的标签名已存在")
    old_record = deepcopy(old_item)
    old_item.item_name = edit_item.item_name
    old_item.item_label = edit_item.item_label
    new_record = deepcopy(old_item)
    db.add(old_item)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_record, old_object=old_record,
                                 ip=request.client.host)
    return {"message": "属性修改成功"}


@cmdb_router.get('/instance_lists', name="模型下实例列表")
async def instance_lists(type_id: str, db: Session = Depends(get_db),
                         current_user: User = Depends(check_perm('/cmdb/instance_lists'))):
    # 获取所有实例
    instances = db.query(CMDBRecord).filter(CMDBRecord.cmdb_type_id == int(type_id)).all()
    # id转为str
    for instance in instances:
        instance.cmdb_record_id = str(instance.cmdb_record_id)
        instance.cmdb_type_id = str(instance.cmdb_type_id)
    # 获取类型下面所有属性
    items = db.query(CMDBItem).filter(CMDBItem.cmdb_type_id == int(type_id)).all()
    return {"instances": instances, "items": items}


@cmdb_router.put('/add_record', name="新增记录")
async def add_record(request: Request, new_record: Dict[str, str], db: Session = Depends(get_db),
                     current_user: User = Depends(check_perm('/cmdb/add_record'))):
    type_id = int(new_record.get("cmdb_type_id", "0"))
    if type_id == 0:
        raise HTTPException(status_code=406, detail="请传入cmdb_type_id")
    # 删除id就是记录详情了
    del new_record['cmdb_type_id']
    cmdb_record = CMDBRecord()
    cmdb_record.cmdb_type_id = type_id
    cmdb_record.cmdb_record_detail = new_record
    record = deepcopy(cmdb_record)
    db.add(cmdb_record)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=record, ip=request.client.host)
    return {"message": "实例添加成功"}


@cmdb_router.post('/edit_record', name="修改记录")
async def edit_instance(request: Request, edit_record: Dict[str, str], db: Session = Depends(get_db),
                        current_user: User = Depends(check_perm('/cmdb/edit_record'))):
    type_id = int(edit_record.get("cmdb_type_id", "0"))
    record_id = int(edit_record.get("cmdb_record_id", "0"))
    if type_id == 0 or record_id == 0:
        raise HTTPException(status_code=406, detail="请传入id")
    # 删除id就是记录详情了
    del edit_record["cmdb_type_id"]
    del edit_record["cmdb_record_id"]
    instance = db.query(CMDBRecord).filter(CMDBRecord.cmdb_record_id == record_id).first()
    old_record = deepcopy(instance)
    instance.cmdb_record_detail = edit_record
    new_record = deepcopy(instance)
    db.add(instance)
    db.commit()
    Record.create_operate_record(username=current_user.username, new_object=new_record, old_object=old_record,
                                 ip=request.client.host)
    return {"message": "实例修改成功"}


@cmdb_router.delete('/delete_record', name="删除记录")
async def delete_record(request: Request, record_id: str, db: Session = Depends(get_db),
                        current_user: User = Depends(check_perm('/cmdb/delete_record'))):
    record = db.query(CMDBRecord).filter(CMDBRecord.cmdb_record_id == int(record_id)).first()
    if not record:
        raise HTTPException(status_code=406, detail="要删除的ID不存在")
    old_record = deepcopy(record)
    db.delete(record)
    db.commit()
    Record.create_operate_record(username=current_user.username, old_object=old_record, ip=request.client.host)
    return {"message": "记录删除成功"}


@cmdb_router.get('/record_details/{record_id}', name="获取记录详情")
async def get_record_details(record_id: str, db: Session = Depends(get_db),
                             current_user: User = Depends(check_perm('/cmdb/record_details'))):
    record_item = db.query(CMDBRecord).filter(CMDBRecord.cmdb_record_id == int(record_id)).first()
    if not record_item:
        raise HTTPException(status_code=406, detail="此ID信息不存在")
    return {"message": "ok", "record_details": record_item.cmdb_record_detail}


@cmdb_router.websocket('/web_terminal', name="网页终端")
async def web_ssh(websocket: WebSocket, username: str, password: str, ip: str, port: str,
                  db: Session = Depends(get_db)):
    await websocket.accept()
    # 连接服务器
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip, int(port), username, password)
    transport = ssh_client.get_transport()
    chan = transport.open_session()
    chan.get_pty(term='ansi', width=80, height=40)
    chan = ssh_client.invoke_shell()

    async def send_ssh():
        try:
            while True:
                result = chan.recv(2048).decode('utf-8')
                await websocket.send_text(result)
        except Exception:
            pass

    # 初次连接，有两条信息返回，一个是上次登录信息，一个是默认信息
    for i in range(2):
        login_data = chan.recv(2048).decode('utf-8')
        await websocket.send_text(login_data)
    # 启动多线程接收ssh返回的信息
    Thread(target=asyncio.run, args=(send_ssh(),)).start()
    Thread(target=asyncio.run, args=(send_ssh(),)).start()
    try:
        while True:
            data = await websocket.receive_text()
            chan.send(data)
    except Exception as ex:
        print(f"websocket closed:{str(ex)}")
        await websocket.close()
        ssh_client.close()
