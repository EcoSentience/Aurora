from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ....models.chat import ChatMessage, ChatResponse
from ....services.chat_service import ChatService
from ....core.auth import get_current_user
from ....core.rate_limiter import RateLimiter

router = APIRouter(prefix="/v1/chat", tags=["chat"])
chat_service = ChatService()
rate_limiter = RateLimiter()

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(
    message: ChatMessage,
    current_user = Depends(get_current_user)
):
    """
    Process chat messages with Aurora's environmental intelligence.
    
    This endpoint handles:
    - Environmental query processing
    - Context-aware responses
    - Biodiversity data integration
    """
    try:
        # Apply rate limiting
        await rate_limiter.check_limit(current_user.id)
        
        # Process message
        response = await chat_service.process_message(message)
        
        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing environmental query: {str(e)}"
        )

@router.get("/context", response_model=List[str])
async def get_environmental_context(
    current_user = Depends(get_current_user)
):
    """
    Retrieve available environmental context categories for chat enhancement.
    """
    try:
        context_categories = [
            "biodiversity_metrics",
            "conservation_status",
            "ecological_indicators",
            "species_interactions"
        ]
        return context_categories
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching environmental context: {str(e)}"
        )