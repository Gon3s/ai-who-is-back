from pydantic import BaseModel


class Character(BaseModel):
    """Character model representing a person in the game"""

    id: int
    name: str
    hair_color: str
    hair_style: str
    eye_color: str
    has_glasses: bool
    has_beard: bool
    has_hat: bool
    has_earring: bool
    gender: str
    style: str
    skin_tone: str
