from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, JSON
from utils.snow_flake import generate_id
from datetime import datetime


class CMDBType(Base):
    __tablename__ = "cmdb_type"
    __table_args__ = ({"comment": "CMDB类型表"})
    cmdb_type_id = Column(BigInteger, primary_key=True, index=True, default=generate_id, unique=True,
                          comment="cmdb类型id")
    cmdb_type_name = Column(String(100), nullable=False, comment="cmdb类型名")
    cmdb_type_label = Column(String(100), nullable=False, comment="cmdb类型显示名")
    cmdb_type_icon = Column(String(20), comment="显示图标")
    creat_time = Column(DateTime(), default=datetime.now, comment="创建时间")
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now, comment="最后一次更新时间")

    def __repr__(self):
        return f"CMDBType:{self.cmdb_type_name}"


class CMDBItem(Base):
    __tablename__ = "cmdb_item"
    __table_args__ = ({"comment": "CMDB具体属性表"})
    item_id = Column(BigInteger, primary_key=True, index=True, default=generate_id, unique=True,
                          comment="cmdb属性id")
    item_name = Column(String(20), comment="cmbd类型属性名")
    item_label = Column(String(20), comment="cmdb类型属性label")
    cmdb_type_id = Column(BigInteger, comment="cmdb类型id")
    creat_time = Column(DateTime(), default=datetime.now, comment="创建时间")
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now, comment="最后一次更新时间")


class CMDBRecord(Base):
    __tablename__ = "cmdb_record"
    __table_args__ = ({"comment": "CMDB数据记录表"})
    cmdb_record_id = Column(BigInteger, primary_key=True, index=True, default=generate_id, unique=True,
                            comment="cmdb记录id")
    cmdb_record_detail = Column(JSON,comment="cmdb记录详情")
    cmdb_type_id = Column(BigInteger, comment="cmdb类型id")
