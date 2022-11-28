from fastapi import APIRouter

from .endpoints import login, users, home, builders  # noqa F401

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(builders.router, prefix="/builders", tags=["builders"])
