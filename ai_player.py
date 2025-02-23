import asyncio
from typing import Dict
import logging
from prompt_manager import PromptManager
from config import LLMConfig

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class AIPlayer:
    def __init__(self, character: Dict, config: LLMConfig):
        self.character = character
        self.prompt_manager = PromptManager(config)
        self.system_prompt = self.prompt_manager.create_system_prompt(character)
        logger.info("AI Player initialized with secret character")

    def answer_question(self, question: str) -> str:
        """Répond à une question en utilisant le LLM."""
        answer = self.prompt_manager.get_answer(self.system_prompt, question)
        if answer is None:
            return "Je ne peux pas répondre à cette question pour le moment."
        return answer
