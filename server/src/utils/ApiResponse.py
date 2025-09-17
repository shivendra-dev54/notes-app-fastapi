from pydantic import BaseModel
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    """
    A generic response model for standardizing API outputs.
    """
    status: int = 200
    message: str = ""
    data: Optional[T] = None
    success: bool = True

    @staticmethod
    def success_response(data: T = None, message: str = "Success"):
        return APIResponse(status=200, message=message, data=data, success=True)

    @staticmethod
    def error_response(message: str = "Error", status: int = 400):
        return APIResponse(status=status, message=message, data=None, success=False)
