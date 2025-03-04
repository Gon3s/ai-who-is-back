from typing import Optional
from groq import Groq
from models.character import Character
from models.responses import ValidResponse
from utils.logger import get_app_logger
from utils.config import Settings

logger = get_app_logger(__name__)


class PromptManager:
    """Manages interactions with the Groq API for the Who Is It game."""

    def __init__(self, config: Settings) -> None:
        """
        Initializes the prompt manager.

        Args:
            config: Configuration containing API parameters
        """
        if not config.api_key:
            raise ValueError("API key is required")
        self.client = Groq(api_key=config.api_key)
        self.config = config

    def create_system_prompt(self, character: Character) -> str:
        """Creates the system prompt that defines the context for the LLM."""
        return f"""Tu es un assistant qui joue au jeu "Qui est-ce?". 
Tu as choisi le personnage suivant :
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

INSTRUCTIONS IMPORTANTES:
1. Réponds UNIQUEMENT par un seul mot : "Oui", "Non", ou "Je ne peux pas répondre".
2. Ne donne AUCUNE explication ou contexte.
3. Ne montre PAS ton raisonnement.
4. Ne révèle JAMAIS le nom ou les caractéristiques du personnage.
5. Reste STRICTEMENT dans ce format de réponse."""

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

    def get_answer(self, system_prompt: str, question: str) -> Optional[ValidResponse]:
        """
        Gets a response from the Groq API.

        Args:
            system_prompt: The system prompt defining the context
            question: The question asked by the player

        Returns:
            The validated response or None in case of error

        Raises:
            groq.APIError: In case of API error
        """
        try:
            if not question.strip():
                logger.warning("Empty question received")
                return None

            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question},
                ],
                model=self.config.model_name,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )

            logger.debug(f"Raw API response: {response}")

            if not response.choices:
                logger.error("No response received from API")
                return None

            raw_response = response.choices[0].message.content
            logger.debug(f"Raw response: {raw_response}")

            return self.clean_response(raw_response)

        except Exception as e:
            logger.error(f"Error during Groq API call: {str(e)}")
            return None
