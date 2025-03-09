from typing import List, Optional
from pydantic import BaseModel

from src.models.character import Character


class GameResponse(BaseModel):
    """API response model for game initialization"""

    game_id: str
    characters: List[Character]
    message: str = "Game initialized successfully"
    debug: Optional[Character]


class QuestionRequest(BaseModel):
    """API request model for asking a question"""

    game_id: str
    question: str


class QuestionResponse(BaseModel):
    """API response model for question answers"""

    answer: str
    remaining_attempts: int


class GuessRequest(BaseModel):
    """API request model for making a character guess"""

    game_id: str
    character_name: str


class GuessResponse(BaseModel):
    """API response model for guess results"""

    is_correct: bool
    message: str
    remaining_attempts: int
