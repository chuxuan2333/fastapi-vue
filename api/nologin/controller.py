from fastapi import APIRouter


nologin_router = APIRouter()


@nologin_router.get("/hello/{name}", dependencies=[])
async def hello():
    return {"name": "Hello World"}
