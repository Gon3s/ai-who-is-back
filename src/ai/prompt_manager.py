from typing import Optional, Literal
from groq import Groq
import logging
import re
from models.character import Character
from utils.config import Settings

logger = logging.getLogger(__name__)

ValidResponse = Literal["Oui", "Non", "Je ne peux pas répondre"]

class PromptManager:
    """Gère les interactions avec l'API Groq pour le jeu Qui est-ce."""

    def __init__(self, config: Settings) -> None:
        """
        Initialise le gestionnaire de prompts.

        Args:
            config: Configuration contenant les paramètres de l'API
        """
        if not config.api_key:
            raise ValueError("API key is required")
        self.client = Groq(api_key=config.api_key)
        self.config = config

    def create_system_prompt(self, character: Character) -> str:
        """Crée le prompt système qui définit le contexte pour le LLM."""
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
        Nettoie et valide la réponse de l'API.

        Args:
            response: Réponse brute de l'API

        Returns:
            Une réponse valide parmi: "Oui", "Non", "Je ne peux pas répondre"
        """
        response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
        response = response.strip().lower()

        response_mapping = {
            "oui": "Oui",
            "non": "Non",
            "je ne peux pas répondre": "Je ne peux pas répondre",
        }

        return response_mapping.get(response, "Je ne peux pas répondre")

    def get_answer(self, system_prompt: str, question: str) -> Optional[ValidResponse]:
        """
        Obtient une réponse de l'API Groq.

        Args:
            system_prompt: Le prompt système définissant le contexte
            question: La question posée par le joueur

        Returns:
            La réponse validée ou None en cas d'erreur

        Raises:
            groq.APIError: En cas d'erreur de l'API
        """
        try:
            if not question.strip():
                logger.warning("Question vide reçue")
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

            if not response.choices:
                logger.error("Aucune réponse reçue de l'API")
                return None

            raw_response = response.choices[0].message.content
            logger.debug(f"Réponse brute: {raw_response}")

            return self.clean_response(raw_response)

        except Exception as e:
            logger.error(f"Erreur lors de l'appel à Groq: {str(e)}")
            return None
