from pydantic import BaseModel
from typing import Optional


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
    image_url: Optional[str] = None

    def get_image_url(self) -> str:
        """
        Generate the URL for the character image.

        Returns:
            str: URL to access the character image
        """
        filename = self.name.lower().replace(" ", "_")
        return f"/images/{filename}.jpg"

    def __init__(self, **data):
        """Initialize character and set default image path if not provided."""
        super().__init__(**data)
        self.image_url = self.get_image_url()
