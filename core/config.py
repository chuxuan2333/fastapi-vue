# -*- coding:utf-8 -*-

from pydantic import AnyHttpUrl
from typing import List
from loguru import logger
import time
import os


class Settings:
    ENV = os.environ.get("fast_env", "DEV")  # 本次启动环境
    APP_NAME = "fastapi-vue-admin"
    # api前缀
    API_PREFIX = "/api"
    # jwt密钥,建议随机生成一个
    SECRET_KEY = "ShsUP9qIP2Xui2GpXRY6y74v2JSVS0Q2YOXJ22VjwkI"
    # token过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
    # 跨域白名单
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:9528", "http://localhost:8999"]
    # db配置
    DB_URL = "mysql+pymysql://root:root@127.0.0.1:3306/fast"
    # 启动端口配置
    PORT = 8999
    # 是否热加载
    RELOAD = True
    # 上传文件存储位置
    UPLOAD_FOLDER = "D:\\code\\upload_files"
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    # CMDB模板文件存储位置
    CMDB_FOLDER = "D:\\code\\cmdb_files"
    if not os.path.exists(CMDB_FOLDER):
        os.mkdir(CMDB_FOLDER)
    # 日志收集器
    LOG_FOLDER = "D:\\code\\fastapi-logs"
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)
    t = time.strftime("%Y_%m_%d")
    logger = logger
    logger.add(f"{LOG_FOLDER}/fastapi_log_{t}.log", rotation="00:00", encoding="utf-8", retention="30 days")


settings = Settings()
