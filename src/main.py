import os

from core.config import LLMConfig
from game.game import check_victory, get_user_input, initialize_game


def main():
    print("Bienvenue dans AI Who Is!")
    print(
        "Posez des questions auxquelles je répondrai par Oui ou Non pour deviner le personnage mystère."
    )

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

        if user_input.lower() in ["quit", "q", "exit"]:
            print("Merci d'avoir joué !")
            break

        if is_proposal:
            victory = check_victory(user_input, secret_character)
            result = "Correct!" if victory else "Incorrect"
            game_logger.log_interaction(attempts, user_input, result, is_proposal=True)

            if victory:
                print(
                    f"\nFélicitations ! Vous avez trouvé le personnage mystère en {attempts} tentatives !"
                )
                print(f"C'était bien {secret_character['name']} !")
                break
            else:
                print(
                    "\nDésolé, ce n'est pas le bon personnage. Continuez à chercher !"
                )
                if attempts == max_attempts:
                    print(
                        f"\nGame Over ! Le personnage était {secret_character['name']} !"
                    )
                continue

        else:
            answer = ai_player.answer_question(user_input)
            game_logger.log_interaction(attempts, user_input, answer)
            print(f"\nRéponse : {answer}")

        if attempts == max_attempts:
            print(f"\nGame Over ! Le personnage était {secret_character['name']} !")


if __name__ == "__main__":
    main()
