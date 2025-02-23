import json
import random
from typing import List, Dict
from ai_player import AIPlayer
import asyncio
import os
from dotenv import load_dotenv
from config import LLMConfig
from game_logger import GameLogger

# Charger les variables d'environnement au démarrage
load_dotenv()

def load_characters() -> List[Dict]:
    """Charge la liste des personnages depuis le fichier JSON."""
    with open('data/stub_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['characters']

def select_game_characters(characters: List[Dict], num_characters: int = 9) -> List[Dict]:
    """Sélectionne aléatoirement un nombre spécifique de personnages."""
    return random.sample(characters, num_characters)

def choose_character_to_guess(characters: List[Dict]) -> Dict:
    """Choisit aléatoirement un personnage à deviner parmi la liste."""
    return random.choice(characters)

def display_character(character: Dict) -> str:
    """Affiche les détails d'un personnage de manière formatée."""
    return f"""
    {character['name']}:
    - Cheveux: {character['hair']}
    - Yeux: {character['eyes']}
    - Lunettes: {'Oui' if character['glasses'] else 'Non'}
    - Barbe: {'Oui' if character['beard'] else 'Non'}
    - Chapeau: {'Oui' if character['hat'] else 'Non'}
    """

def display_game_characters(characters: List[Dict]):
    """Affiche tous les personnages du jeu."""
    print("\nPersonnages en jeu:")
    print("="*50)
    for i, character in enumerate(characters, 1):
        print(f"\nPersonnage {i}:{display_character(character)}")
    print("="*50)

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
    return proposed_name.lower() == secret_character['name'].lower()

def main():
    print("Bienvenue dans AI Who Is!")
    print("Posez des questions auxquelles je répondrai par Oui ou Non pour deviner le personnage mystère.")
    
    api_key = os.getenv("AIWHO_API_KEY")
    if not api_key:
        print("Erreur: La clé API n'est pas définie dans le fichier .env")
        return
        
    config = LLMConfig(api_key=api_key)
    characters, secret_character, ai_player, game_logger = initialize_game(config)
    
    max_attempts = 20
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nTentative {attempts}/{max_attempts}")
        
        user_input, is_proposal = get_user_input()
        
        if user_input.lower() in ['quit', 'q', 'exit']:
            print("Merci d'avoir joué !")
            break
            
        if is_proposal:
            victory = check_victory(user_input, secret_character)
            result = "Correct!" if victory else "Incorrect"
            game_logger.log_interaction(attempts, user_input, result, is_proposal=True)
            
            if victory:
                print(f"\nFélicitations ! Vous avez trouvé le personnage mystère en {attempts} tentatives !")
                print(f"C'était bien {secret_character['name']} !")
                break
            else:
                print("\nDésolé, ce n'est pas le bon personnage. Continuez à chercher !")
                if attempts == max_attempts:
                    print(f"\nGame Over ! Le personnage était {secret_character['name']} !")
                continue
                
        else:
            answer = ai_player.answer_question(user_input)
            game_logger.log_interaction(attempts, user_input, answer)
            print(f"\nRéponse : {answer}")
        
        if attempts == max_attempts:
            print(f"\nGame Over ! Le personnage était {secret_character['name']} !")

if __name__ == "__main__":
    main()
