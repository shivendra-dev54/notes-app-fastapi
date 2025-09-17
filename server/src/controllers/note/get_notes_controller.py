from fastapi import Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.config.db_connect import get_db
from src.db.schemas.note_schema import Note
from src.utils.ApiResponse import APIResponse
from src.middlewares.auth_middleware import get_current_user

async def get_notes_controller(response: Response, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    result = await db.execute(select(Note).where(Note.user_id == current_user.id))
    notes = result.scalars().all()
    
    return APIResponse.success_response(
        message="Notes fetched successfully",
        data=[{"id": n.id, "content": n.content, "created_at": n.created_at, "updated_at": n.updated_at} for n in notes]
    ).model_dump()
