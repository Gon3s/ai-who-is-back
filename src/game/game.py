import json
import random
import logging
from typing import List, Dict, Optional
from pathlib import Path
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

class GameManager:
    """Gère les opérations principales du jeu."""

    def __init__(self, data_file: str = "data/stub_data.json"):
        """
        Initialise le gestionnaire de jeu.

        Args:
            data_file (str): Chemin vers le fichier de données des personnages
        """
        load_dotenv()
        self.data_file = Path(data_file)
        self.characters: List[Dict] = []
        self._load_characters()

    def _load_characters(self) -> None:
        """Charge la liste des personnages depuis le fichier JSON."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.characters = data["characters"]
                logger.info(f"Chargé {len(self.characters)} personnages avec succès")
        except FileNotFoundError:
            logger.error(f"Fichier de données non trouvé: {self.data_file}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Erreur de décodage JSON du fichier: {self.data_file}")
            raise
        except KeyError:
            logger.error("La clé 'characters' n'existe pas dans le fichier JSON")
            raise

    def select_game_characters(self, num_characters: int = 9) -> Optional[List[Dict]]:
        """
        Sélectionne aléatoirement un nombre spécifique de personnages.

        Args:
            num_characters (int): Nombre de personnages à sélectionner

        Returns:
            Optional[List[Dict]]: Liste des personnages sélectionnés ou None en cas d'erreur
        """
        try:
            if len(self.characters) < num_characters:
                logger.error(
                    f"Pas assez de personnages disponibles. Requis: {num_characters}, Disponible: {len(self.characters)}"
                )
                return None
            selected = random.sample(self.characters, num_characters)
            logger.info(f"Sélectionné {num_characters} personnages pour la partie")
            return selected
        except Exception as e:
            logger.error(f"Erreur lors de la sélection des personnages: {str(e)}")
            return None

    def choose_character_to_guess(self, game_characters: List[Dict]) -> Optional[Dict]:
        """
        Choisit aléatoirement un personnage à deviner parmi la liste.

        Args:
            game_characters (List[Dict]): Liste des personnages disponibles

        Returns:
            Optional[Dict]: Personnage choisi ou None en cas d'erreur
        """
        try:
            if not game_characters:
                logger.error("La liste des personnages est vide")
                return None
            character = random.choice(game_characters)
            logger.info("Personnage mystère sélectionné avec succès")
            return character
        except Exception as e:
            logger.error(f"Erreur lors du choix du personnage mystère: {str(e)}")
            return None


