import json
import random
from typing import List, Dict
from ai.ai_player import AIPlayer
from dotenv import load_dotenv
from core.config import LLMConfig
from core.game_logger import GameLogger

# Charger les variables d'environnement au démarrage
load_dotenv()


def load_characters() -> List[Dict]:
    """Charge la liste des personnages depuis le fichier JSON."""
    with open("data/stub_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data["characters"]


def select_game_characters(
    characters: List[Dict], num_characters: int = 9
) -> List[Dict]:
    """Sélectionne aléatoirement un nombre spécifique de personnages."""
    return random.sample(characters, num_characters)


def choose_character_to_guess(characters: List[Dict]) -> Dict:
    """Choisit aléatoirement un personnage à deviner parmi la liste."""
    return random.choice(characters)


def display_character(character: Dict) -> str:
    """Affiche les détails d'un personnage de manière formatée."""
    return f"""
    {character["name"]}:
    - Cheveux: {character["hair"]}
    - Yeux: {character["eyes"]}
    - Lunettes: {"Oui" if character["glasses"] else "Non"}
    - Barbe: {"Oui" if character["beard"] else "Non"}
    - Chapeau: {"Oui" if character["hat"] else "Non"}
    """


def display_game_characters(characters: List[Dict]):
    """Affiche tous les personnages du jeu."""
    print("\nPersonnages en jeu:")
    print("=" * 50)
    for i, character in enumerate(characters, 1):
        print(f"\nPersonnage {i}:{display_character(character)}")
    print("=" * 50)


def initialize_game(config: LLMConfig):
    """Initialise le jeu en sélectionnant les personnages."""
    game_logger = GameLogger()
    all_characters = load_characters()
    game_characters = select_game_characters(all_characters)
    character_to_guess = choose_character_to_guess(game_characters)
    ai_player = AIPlayer(character_to_guess, config)

    # Log des informations de début de partie
    game_logger.log_game_start(game_characters, character_to_guess)

    print("\nJeu initialisé avec succès!")
    print(f"Nombre de personnages en jeu : {len(game_characters)}")
    display_game_characters(game_characters)
    print("\nLe personnage à deviner a été choisi...")
    return game_characters, character_to_guess, ai_player, game_logger


def get_user_input() -> tuple[str, bool]:
    """Demande une question ou une proposition de personnage à l'utilisateur."""
    print("\nQue souhaitez-vous faire ?")
    print("1. Poser une question (qui peut être répondue par Oui/Non)")
    print("2. Proposer un personnage")
    print("3. Quitter")

    choice = input("Votre choix (1/2/3) : ").strip()

    if choice == "3":
        return "quit", False
    elif choice == "2":
        name = input("Quel est le nom du personnage ? : ").strip()
        return name, True
    else:
        question = input("Votre question : ").strip()
        return question, False


def check_victory(proposed_name: str, secret_character: Dict) -> bool:
    """Vérifie si le joueur a deviné le bon personnage."""
    return proposed_name.lower() == secret_character["name"].lower()
