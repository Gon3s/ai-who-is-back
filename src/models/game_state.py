from typing import List
from pydantic import BaseModel
from models.character import Character


class GameState(BaseModel):
    """Represents the current state of a game session"""

    game_id: str
    characters: List[Character]
    secret_character: Character
    attempts: int = 0
