from fastapi import Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.db_connect import get_db
from src.db.schemas.note_schema import Note
from src.utils.ApiResponse import APIResponse
from src.routes.schemas import NoteCreateRequest
from src.middlewares.auth_middleware import get_current_user

async def create_note_controller(
    payload: NoteCreateRequest, 
    response: Response, 
    db: AsyncSession = Depends(get_db), 
    current_user=Depends(get_current_user)
):
    note = Note(
        user_id=current_user.id,
        content=payload.content
    )
    db.add(note)
    await db.commit()
    await db.refresh(note)

    return APIResponse.success_response(
        message="Note created successfully",
        data={
            "id": note.id, 
            "content": note.content, 
            "created_at": note.created_at
        }
    ).model_dump()
