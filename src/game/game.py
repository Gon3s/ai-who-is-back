import json
import random
from typing import List, Dict, Optional
from pathlib import Path
from dotenv import load_dotenv

from src.utils.logger import get_app_logger

logger = get_app_logger(__name__)

class GameManager:
    """Manages the main game operations."""

    def __init__(self, data_file: str = "data/stub_data.json"):
        """
        Initializes the game manager.

        Args:
            data_file (str): Path to the character data file
        """
        load_dotenv()
        self.data_file = Path(data_file)
        self.characters: List[Dict] = []
        self._load_characters()

    def _load_characters(self) -> None:
        """Loads the list of characters from the JSON file."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.characters = data["characters"]

                logger.info(f"Successfully loaded {len(self.characters)} characters")
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_file}")
            raise
        except json.JSONDecodeError:
            logger.error(f"JSON decoding error in file: {self.data_file}")
            raise
        except KeyError:
            logger.error("The 'characters' key does not exist in the JSON file")
            raise

    def select_game_characters(self, num_characters: int = 9) -> Optional[List[Dict]]:
        """
        Randomly selects a specific number of characters.

        Args:
            num_characters (int): Number of characters to select

        Returns:
            Optional[List[Dict]]: List of selected characters or None in case of error
        """
        try:
            if len(self.characters) < num_characters:
                logger.error(
                    f"Not enough characters available. Required: {num_characters}, Available: {len(self.characters)}"
                )
                return None
            selected = random.sample(self.characters, num_characters)
            logger.info(f"Selected {num_characters} characters for the game")
            return selected
        except Exception as e:
            logger.error(f"Error while selecting characters: {str(e)}")
            return None

    def choose_character_to_guess(self, game_characters: List[Dict]) -> Optional[Dict]:
        """
        Randomly chooses a character to be guessed from the list.

        Args:
            game_characters (List[Dict]): List of available characters

        Returns:
            Optional[Dict]: Chosen character or None in case of error
        """
        try:
            if not game_characters:
                logger.error("The character list is empty")
                return None
            character = random.choice(game_characters)
            logger.info("Mystery character successfully selected")
            logger.debug(f"Mystery character: {character}")
            return character
        except Exception as e:
            logger.error(f"Error while choosing mystery character: {str(e)}")
            return None


