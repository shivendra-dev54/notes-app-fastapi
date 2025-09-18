from fastapi import APIRouter, Depends, Response, Cookie
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.user.sign_in_controller import sign_in_controller
from src.controllers.user.sign_up_controller import sign_up_controller
from src.controllers.user.refresh_controller import refresh_token_controller
from src.controllers.user.logout_controller import logout_controller

from src.routes.schemas import SignInRequest, SignUpRequest
from src.config.db_connect import get_db

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

# --- SIGN UP ---
@user_router.post("/sign_up", response_model=dict)
async def sign_up(
    payload: SignUpRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    return await sign_up_controller(payload, response, db)


# --- SIGN IN ---
@user_router.post("/sign_in", response_model=dict)
async def sign_in(
    payload: SignInRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    return await sign_in_controller(payload, response, db)


# --- REFRESH ---
@user_router.put("/refresh", response_model=dict)
async def refresh(
    response: Response,
    refresh_token: str | None = Cookie(default=None),
    db: AsyncSession = Depends(get_db),
):
    return await refresh_token_controller(
        response, 
        db=db,
        refresh_token=refresh_token
        )


# --- LOGOUT ---
@user_router.post("/logout", response_model=dict)
async def logout(
    response: Response,
    access_token: str | None = Cookie(default=None),
    db: AsyncSession = Depends(get_db),
):
    return await logout_controller(
        response=response, 
        db=db,
        access_token=access_token
    )
