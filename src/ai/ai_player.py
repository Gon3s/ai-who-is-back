from typing import Optional

from src.ai.langchain_manager import LangChainManager
from src.models.character import Character
from src.models.responses import ValidResponse
from src.utils.config import Settings
from src.utils.logger import get_app_logger

logger = get_app_logger(__name__)


class AIPlayer:
    def __init__(self, character: Character, config: Settings):
        """
        Initialize the AI player with the given character and configuration.

        Args:
            character: The character to be guessed
            config: Application settings including LLM parameters
        """
        self.character = character
        self.langchain_manager = LangChainManager(config)

    def answer_question(self, question: str) -> Optional[ValidResponse]:
        """
        Process a question and return the AI's answer.

        Args:
            question: The question asked by the player

        Returns:
            Optional[ValidResponse]: A valid response from the ValidResponse enum
        """
        logger.info("Processing question using LangChain")
        return self.langchain_manager.get_answer(self.character, question)
