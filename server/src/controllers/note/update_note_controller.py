from fastapi import Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.config.db_connect import get_db
from src.db.schemas.note_schema import Note
from src.utils.ApiResponse import APIResponse
from src.routes.schemas import NoteUpdateRequest
from src.middlewares.auth_middleware import get_current_user
from fastapi import HTTPException

async def update_note_controller(
    note_id: int, 
    payload: NoteUpdateRequest, 
    response: Response, 
    db: AsyncSession = Depends(get_db), 
    current_user=Depends(get_current_user)
):
    result = await db.execute(select(Note).where(Note.id == note_id, Note.user_id == current_user.id))
    note = result.scalars().first()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    note.content = payload.content
    await db.commit()
    await db.refresh(note)

    return APIResponse.success_response(
        message="Note updated successfully",
        data={"id": note.id, "content": note.content, "updated_at": note.updated_at}
    ).model_dump()
