from typing import Dict, Optional
from groq import Groq
import logging
import re
from utils.config import Settings

logger = logging.getLogger(__name__)


class PromptManager:
    def __init__(self, config: Settings):
        self.client = Groq(api_key=config.api_key)
        self.config = config

    def create_system_prompt(self, character: Dict) -> str:
        """Crée le prompt système qui définit le contexte pour le LLM."""
        return f"""Tu es un assistant qui joue au jeu "Qui est-ce?". 
Tu as choisi le personnage suivant :
- Nom: {character["name"]}
- Cheveux: {character["hair"]}
- Yeux: {character["eyes"]}
- Lunettes: {"Oui" if character["glasses"] else "Non"}
- Barbe: {"Oui" if character["beard"] else "Non"}
- Chapeau: {"Oui" if character["hat"] else "Non"}

INSTRUCTIONS IMPORTANTES:
1. Réponds UNIQUEMENT par un seul mot : "Oui", "Non", ou "Je ne peux pas répondre".
2. Ne donne AUCUNE explication ou contexte.
3. Ne montre PAS ton raisonnement.
4. Ne révèle JAMAIS le nom ou les caractéristiques du personnage.
5. Reste STRICTEMENT dans ce format de réponse."""

    def clean_response(self, response: str) -> str:
        """Nettoie la réponse pour ne garder que Oui/Non/Je ne peux pas répondre."""
        # Supprime les balises <think> et leur contenu
        response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
        # Supprime tous les espaces et sauts de ligne en trop
        response = response.strip()

        # Vérifie si la réponse correspond à l'un des formats valides
        valid_responses = {"oui", "non", "je ne peux pas répondre"}
        clean_response = response.lower()

        if clean_response in valid_responses:
            return response.capitalize()
        return "Je ne peux pas répondre"

    def get_answer(self, system_prompt: str, question: str) -> Optional[str]:
        """Obtient une réponse de Groq pour une question donnée."""
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question},
                ],
                model=self.config.model_name,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )
            raw_response = completion.choices[0].message.content.strip()
            print(raw_response)
            return self.clean_response(raw_response)

        except Exception as e:
            logger.error(f"Erreur lors de l'appel à Groq: {str(e)}")
            return None
