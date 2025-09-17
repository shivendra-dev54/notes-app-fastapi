from fastapi import Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext

from src.config.db_connect import get_db
from src.db.schemas.user_schema import User
from src.utils.ApiResponse import APIResponse
from src.routes.schemas import SignUpRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def sign_up_controller(payload: SignUpRequest, response: Response, db: AsyncSession = Depends(get_db)):
    # check if user exists
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing_user = result.scalars().first()
    if existing_user:
        return APIResponse.error_response(message="User already exists", status_code=400).model_dump()

    # hash password
    hashed_password = pwd_context.hash(payload.password)

    # create user
    user = User(
        username=payload.username,
        email=payload.email,
        password=hashed_password
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return APIResponse.success_response(
        message="User registered successfully",
        data={"id": user.id, "username": user.username, "email": user.email}
    ).model_dump()
