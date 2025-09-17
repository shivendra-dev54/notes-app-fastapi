from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.db_connect import get_db
from src.middlewares.auth_middleware import get_current_user
from src.routes.schemas import NoteCreateRequest, NoteUpdateRequest
from src.controllers.note.add_note_controller import create_note_controller
from src.controllers.note.get_notes_controller import get_notes_controller
from src.controllers.note.update_note_controller import update_note_controller
from src.controllers.note.delete_note_controller import delete_note_controller

note_router = APIRouter(
    prefix="/note",
    tags=["Note"]
)

# Create a note
@note_router.post("/create", response_model=dict)
async def create_note(payload: NoteCreateRequest, response: Response, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await create_note_controller(payload, response, db, current_user)

# Read all notes for the current user
@note_router.get("/read", response_model=dict)
async def read_notes(response: Response, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await get_notes_controller(response, db, current_user)

# Update a note by ID
@note_router.put("/update/{note_id}", response_model=dict)
async def update_note(note_id: int, payload: NoteUpdateRequest, response: Response, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await update_note_controller(note_id, payload, response, db, current_user)

# Delete a note by ID
@note_router.delete("/delete/{note_id}", response_model=dict)
async def delete_note(note_id: int, response: Response, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await delete_note_controller(note_id, response, db, current_user)
