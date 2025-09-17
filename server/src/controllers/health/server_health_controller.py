from src.utils.ApiResponse import APIResponse

# @endpoint: /api/v0/server/health_check
# @method: POST
async def server_health_controller():
    """
    This is an endpoint for checking server health. 
    """
    return APIResponse.success_response(
        message="server running..."
    ).model_dump()
