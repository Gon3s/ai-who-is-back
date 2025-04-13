"""
LangChain integration for AI Who Is game.
"""

from typing import Optional
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.memory import ChatMessageHistory

from src.models.character import Character
from src.models.responses import ValidResponse
from src.utils.logger import get_app_logger
from src.utils.config import Settings

logger = get_app_logger(__name__)


class LangChainManager:
    """Manages LangChain components for the Who Is It game."""

    def __init__(self, config: Settings) -> None:
        """
        Initializes the LangChain manager.

        Args:
            config: Configuration containing API parameters
        """
        if not config.api_key:
            raise ValueError("API key is required")

        self.config = config
        self.llm = ChatGroq(
            api_key=config.api_key,
            model_name=config.model_name,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
        )

        # Initialize output parsers
        self.output_parser = StrOutputParser()

        # Initialize message history for conversation tracking
        self.message_history = ChatMessageHistory()

        logger.info(f"LangChain initialized with model: {config.model_name}")

    def create_decision_chain(self, character: Character) -> RunnableLambda:
        """
        Creates a LangChain decision chain with conversation memory.

        Args:
            character: The character to be guessed

        Returns:
            A runnable chain object
        """
        # Construire un prompt système
        system_template = f"""
Tu dois analyser une question à propos d'un personnage du jeu "Qui est-ce?" et déterminer si la réponse est Oui, Non, ou si tu ne peux pas répondre.

Caractéristiques du personnage:
- Nom: {character.name}
- Couleur de cheveux: {character.hair_color}
- Style de cheveux: {character.hair_style}
- Couleur des yeux: {character.eye_color}
- Lunettes: {"Oui" if character.has_glasses else "Non"}
- Barbe: {"Oui" if character.has_beard else "Non"}
- Chapeau: {"Oui" if character.has_hat else "Non"}
- Boucles d'oreilles: {"Oui" if character.has_earring else "Non"}
- Genre: {character.gender}
- Style vestimentaire: {character.style}
- Teint de peau: {character.skin_tone}

Si la question est trop vague ou ne peut pas être répondue, tu dois répondre "Je ne peux pas répondre".
Si plusieur question sont posées tu dois répondre "Je ne peux pas répondre".s

Tu vas analyser chaque question et répondre UNIQUEMENT par "Oui", "Non", ou "Je ne peux pas répondre".
Ne donne aucune explication supplémentaire.
"""

        def get_answer_from_llm(question_input: str) -> str:
            """Envoie la question au LLM et retourne la réponse."""
            messages = [
                SystemMessage(content=system_template),
                HumanMessage(content=question_input),
            ]

            response = self.llm.invoke(messages)
            return response.content

        # Créer un RunnableLambda qui encapsule toute la logique
        return RunnableLambda(get_answer_from_llm)

    def _update_history(self, question: str, answer: str) -> None:
        """
        Update conversation history with the latest exchange

        Args:
            question: Question asked by the user
            answer: Answer provided by the LLM
        """
        # Add to message history
        self.message_history.add_user_message(question)
        self.message_history.add_ai_message(answer)

    def clean_response(self, response: str) -> ValidResponse:
        """
        Cleans and validates the API response.

        Args:
            response: Raw response from the API

        Returns:
            A valid response from the ValidResponse enum
        """
        if response.endswith("."):
            response = response[:-1]

        response = response.strip().lower()

        response_mapping = {
            "oui": ValidResponse.YES,
            "non": ValidResponse.NO,
            "je ne peux pas répondre": ValidResponse.UNKNOWN,
        }

        logger.debug(f"Cleaned response: {response}")

        return response_mapping.get(response, ValidResponse.UNKNOWN)

    def get_answer(
        self, character: Character, question: str
    ) -> Optional[ValidResponse]:
        """
        Gets a response using the LangChain decision chain.

        Args:
            character: Character object containing all attributes
            question: The question asked by the player

        Returns:
            The validated response or None in case of error
        """
        try:
            if not question.strip():
                logger.warning("Empty question received")
                return None

            # Create the chain
            chain = self.create_decision_chain(character)

            # Execute the chain
            raw_response = chain.invoke(question)

            if not raw_response:
                logger.error("No valid result received from LangChain")
                return None

            # Update conversation history
            self._update_history(question, raw_response)

            logger.debug(f"Raw LangChain response: {raw_response}")

            # Clean and validate the response
            return self.clean_response(raw_response)

        except Exception as e:
            logger.error(f"Error during LangChain execution: {str(e)}")
            return None
