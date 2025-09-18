from fastapi import Response, Cookie, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from jose import JWTError, jwt
from datetime import timedelta

from src.config.db_connect import get_db
from src.db.schemas.user_schema import User
from src.utils.ApiResponse import APIResponse
from src.utils.jwt_handler import SECRET_KEY, ALGORITHM, create_access_token


async def refresh_token_controller(
    response: Response,
    refresh_token: str | None,
    db: AsyncSession
):
    if not refresh_token:
        return APIResponse.error_response(
            message="Refresh token missing", 
            status=401
        ).model_dump()

    # find user by refresh token
    stmt = select(User).where(User.refresh_token == refresh_token)
    result = await db.execute(stmt)
    user = result.scalars().first()
    if not user:
        return APIResponse.error_response(
            message="Invalid refresh token", 
            status=401
        ).model_dump()

    # validate refresh token
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if str(user.id) != user_id:
            raise JWTError()
    except JWTError:
        return APIResponse.error_response(
            message="Invalid refresh token", 
            status=401
        ).model_dump()

    # generate new access token
    access_token = create_access_token({"sub": str(user.id)})

    # update DB
    user.access_token = access_token
    await db.commit()
    await db.refresh(user)

    # set new cookie
    response.set_cookie(
        "access_token", 
        access_token, 
        httponly=True, 
        secure=True, 
        samesite="Lax"
    )

    return APIResponse.success_response(
        message="Access token refreshed"
    ).model_dump()
