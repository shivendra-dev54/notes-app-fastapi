from fastapi import Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext

from src.config.db_connect import get_db
from src.db.schemas.user_schema import User
from src.utils.ApiResponse import APIResponse
from src.routes.schemas import SignInRequest
from src.utils.jwt_handler import create_access_token, create_refresh_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def sign_in_controller(payload: SignInRequest, response: Response, db: AsyncSession = Depends(get_db)):
    """
    Endpoint for signing in an existing user with JWT tokens.
    """

    # 1️⃣ Find user
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalars().first()

    if not user or not pwd_context.verify(payload.password, user.password):
        return APIResponse.error_response(
            message="Invalid email or password",
            status_code=401
        ).model_dump()

    # 2️⃣ Generate tokens
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    # 3️⃣ Save tokens in DB
    user.access_token = access_token
    user.refresh_token = refresh_token
    await db.commit()
    await db.refresh(user)

    # 4️⃣ Set tokens as HttpOnly cookies
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="Lax"
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="Lax"
    )

    # 5️⃣ Success response
    return APIResponse.success_response(
        message="Login successful",
        data={"id": user.id, "username": user.username, "email": user.email}
    ).model_dump()
