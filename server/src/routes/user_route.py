from fastapi import APIRouter

from src.controllers.user.sign_in_controller import sign_in_controller
from src.controllers.user.sign_up_controller import sign_up_controller
from src.controllers.user.refresh_controller import refresh_token_controller
from src.controllers.user.logout_controller import logout_controller

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@user_router.get("/sign_up", response_model=dict)
async def sign_up():
    return await sign_up_controller()

@user_router.get("/sign_in", response_model=dict)
async def sign_in():
    return await sign_in_controller()

@user_router.get("/refresh", response_model=dict)
async def refresh():
    return await refresh_token_controller()

@user_router.get("/logout", response_model=dict)
async def logout():
    return await logout_controller()
