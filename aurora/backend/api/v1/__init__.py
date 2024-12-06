from fastapi import APIRouter
from .chat.routes import router as chat_router

v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(chat_router)