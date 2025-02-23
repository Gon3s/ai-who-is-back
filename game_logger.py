import logging
from typing import List, Dict
from datetime import datetime
import os

class GameLogger:
    def __init__(self):
        """Initialise le logger du jeu."""
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        self.logger = logging.getLogger("game_logger")
        self.logger.setLevel(logging.INFO)
        
        # Création d'un fichier de log avec la date
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        handler = logging.FileHandler(f"logs/game_{timestamp}.log", encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)
        
    def log_game_start(self, characters: List[Dict], secret_character: Dict):
        """Enregistre les informations de début de partie."""
        self.logger.info("=== Nouvelle partie ===")
        self.logger.info("Personnages en jeu :")
        for i, char in enumerate(characters, 1):
            self.logger.info(f"Personnage {i}: {char['name']} - "
                           f"Cheveux: {char['hair']}, "
                           f"Yeux: {char['eyes']}, "
                           f"Lunettes: {'Oui' if char['glasses'] else 'Non'}, "
                           f"Barbe: {'Oui' if char['beard'] else 'Non'}, "
                           f"Chapeau: {'Oui' if char['hat'] else 'Non'}")
        
        self.logger.info("\nPersonnage mystère sélectionné :")
        self.logger.info(f"Nom: {secret_character['name']}")
        self.logger.info(f"Caractéristiques: "
                        f"Cheveux: {secret_character['hair']}, "
                        f"Yeux: {secret_character['eyes']}, "
                        f"Lunettes: {'Oui' if secret_character['glasses'] else 'Non'}, "
                        f"Barbe: {'Oui' if secret_character['beard'] else 'Non'}, "
                        f"Chapeau: {'Oui' if secret_character['hat'] else 'Non'}")
        self.logger.info("==================")
        
    def log_interaction(self, attempt: int, question: str, answer: str, is_proposal: bool = False):
        """Enregistre une interaction (question/réponse ou proposition) du jeu."""
        if is_proposal:
            self.logger.info(f"Tentative {attempt} - Proposition: {question}")
            self.logger.info(f"Résultat: {answer}")
        else:
            self.logger.info(f"Tentative {attempt} - Question: {question}")
            self.logger.info(f"Réponse IA: {answer}")
        self.logger.info("-" * 40)
