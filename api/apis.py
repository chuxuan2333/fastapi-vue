from fastapi import APIRouter
from api.login.controller import login_router
from api.users.controller import user_router
from api.record.controller import record_router
from api.role.controller import role_router
from api.menu.controller import menu_router
from api.perm.controller import perm_router
from api.cmdb.controller import cmdb_router

from api.nologin.controller import nologin_router


api_router = APIRouter()
# router注册
api_router.include_router(login_router, tags=["login"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(record_router, prefix="/record", tags=["record"])
api_router.include_router(role_router, prefix="/role", tags=["role"])
api_router.include_router(menu_router, prefix="/menu", tags=["menu"])
api_router.include_router(perm_router, prefix="/perm", tags=["perm"])
api_router.include_router(cmdb_router, prefix="/cmdb", tags=["cmdb"])

api_router.include_router(nologin_router, tags=["nologin"])

