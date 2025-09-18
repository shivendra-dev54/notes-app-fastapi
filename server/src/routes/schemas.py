from pydantic import BaseModel, EmailStr


class SignInRequest(BaseModel):
    email: EmailStr
    password: str


class SignUpRequest(BaseModel):
    username:str
    email: EmailStr
    password: str


class NoteCreateRequest(BaseModel):
    user_id: int
    content: str


class NoteUpdateRequest(BaseModel):
    content: str


