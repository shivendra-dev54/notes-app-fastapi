from fastapi import Response, Cookie, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.config.db_connect import get_db
from src.db.schemas.user_schema import User
from src.utils.ApiResponse import APIResponse


async def logout_controller(
    response: Response,
    access_token: str | None = Cookie(default=None),
    db: AsyncSession = Depends(get_db)
):
    if access_token:
        stmt = select(User).where(User.access_token == access_token)
        result = await db.execute(stmt)
        user = result.scalars().first()
        if user:
            user.access_token = None
            user.refresh_token = None
            await db.commit()

    # clear cookies
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")

    return APIResponse.success_response(message="Logged out successfully").model_dump()
