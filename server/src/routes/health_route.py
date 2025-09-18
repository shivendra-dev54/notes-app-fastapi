from fastapi import APIRouter
from src.controllers.health.server_health_controller import server_health_controller

health_router = APIRouter(
    prefix="/server",
    tags=["Server Health"]
)

@health_router.get("/health_check", response_model=dict)
async def health_check():
    return await server_health_controller()
