from typing import Optional
import logging
from ai.prompt_manager import PromptManager
from models.character import Character
from utils.config import Settings

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class AIPlayer:
    def __init__(self, character: Character, config: Settings):
        self.prompt_manager = PromptManager(config)
        self.system_prompt = self.prompt_manager.create_system_prompt(character)

    def answer_question(self, question: str) -> Optional[str]:
        """
        Process a question and return the AI's answer.

        Args:
            question: The question asked by the player

        Returns:
            Optional[str]: The AI's response (Yes/No/Cannot answer) or None if error
        """
        return self.prompt_manager.get_answer(self.system_prompt, question)
