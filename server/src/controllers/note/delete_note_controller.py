from fastapi import Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.config.db_connect import get_db
from src.db.schemas.note_schema import Note
from src.utils.ApiResponse import APIResponse
from src.middlewares.auth_middleware import get_current_user
from fastapi import HTTPException

async def delete_note_controller(note_id: int, response: Response, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    result = await db.execute(select(Note).where(Note.id == note_id, Note.user_id == current_user.id))
    note = result.scalars().first()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    await db.delete(note)
    await db.commit()

    return APIResponse.success_response(
        message="Note deleted successfully"
    ).model_dump()
