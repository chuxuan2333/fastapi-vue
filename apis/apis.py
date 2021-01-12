from fastapi import APIRouter
from apis.login.controller import login_router
from apis.users.controller import user_router
from apis.record.controller import record_router
from apis.role.controller import role_router
from apis.menu.controller import menu_router
from apis.perm.controller import perm_router
from apis.cmdb.controller import cmdb_router

api_router = APIRouter()
# router注册
api_router.include_router(login_router, tags=["login"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(record_router, prefix="/record", tags=["record"])
api_router.include_router(role_router, prefix="/role", tags=["role"])
api_router.include_router(menu_router, prefix="/menu", tags=["menu"])
api_router.include_router(perm_router, prefix="/perm", tags=["perm"])
api_router.include_router(cmdb_router, prefix="/cmdb", tags=["cmdb"])
