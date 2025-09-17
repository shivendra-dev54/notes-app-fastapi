from fastapi import FastAPI

# importing routers
from src.routes.health_route import health_router
from src.routes.user_route import user_router
from src.routes.notes_route import note_router


# creating app component
app = FastAPI(title="Heart Notes App")

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