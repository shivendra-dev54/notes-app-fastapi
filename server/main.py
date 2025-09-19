from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# importing routers
from src.routes.health_route import health_router
from src.routes.user_route import user_router
from src.routes.notes_route import note_router


# creating app component
app = FastAPI(title="Heart Notes App")


# CORS setup
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routers
app.include_router(health_router, prefix="/api/v0")
app.include_router(user_router, prefix="/api/v0")
app.include_router(note_router, prefix="/api/v0")


# default route
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the API!"
    }