from typing import List
from pydantic import BaseModel
from models.character import Character


class GameResponse(BaseModel):
    """API response model for game initialization"""

    game_id: str
    characters: List[Character]
    message: str = "Game initialized successfully"


class QuestionRequest(BaseModel):
    """API request model for asking a question"""

    game_id: str
    question: str


class QuestionResponse(BaseModel):
    """API response model for question answers"""

    answer: str
    remaining_attempts: int
