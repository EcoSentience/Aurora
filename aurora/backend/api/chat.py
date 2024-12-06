from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    content: str
    user_id: Optional[str]
    timestamp: Optional[datetime] = datetime.now()
    context: Optional[dict] = {}

class ChatResponse(BaseModel):
    content: str
    sources: Optional[List[str]] = []
    confidence: Optional[float]
    ecological_context: Optional[dict] = {}