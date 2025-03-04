from typing import Optional
from ai.prompt_manager import PromptManager
from models.character import Character
from models.responses import ValidResponse
from utils.config import Settings
from utils.logger import get_app_logger

logger = get_app_logger(__name__)


class AIPlayer:
    def __init__(self, character: Character, config: Settings):
        self.prompt_manager = PromptManager(config)
        self.system_prompt = self.prompt_manager.create_system_prompt(character)

    def answer_question(self, question: str) -> Optional[ValidResponse]:
        """
        Process a question and return the AI's answer.

        Args:
            question: The question asked by the player

        Returns:
            Optional[ValidResponse]: A valid response from the ValidResponse enum
        """
        return self.prompt_manager.get_answer(self.system_prompt, question)
