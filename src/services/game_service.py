import uuid
import logging
from typing import Dict, Tuple, Optional, List
from models.game import GameState, Character
from game.game import GameManager
from ai.ai_player import AIPlayer
from utils.config import get_settings
from utils.exceptions import GameNotFoundError, GameOverError

logger = logging.getLogger(__name__)


class GameService:
    MAX_ATTEMPTS = 20

    def __init__(self) -> None:
        self.games: Dict[str, GameState] = {}
        self.config = get_settings()
        self.game_manager = GameManager()

    def create_game(self) -> Tuple[str, List[Character], Character]:
        """Create a new game session.

        Returns:
            Tuple containing:
            - game_id (str): Unique identifier for the game
            - characters (List[Character]): List of available characters
            - secret_character (Character): Character to be guessed
        """
        try:
            game_characters = self.game_manager.select_game_characters()
            if not game_characters:
                raise ValueError("Failed to select game characters")

            secret_character = self.game_manager.choose_character_to_guess(
                game_characters
            )
            if not secret_character:
                raise ValueError("Failed to select secret character")

            game_characters = [Character(**c) for c in game_characters]
            secret_character = Character(**secret_character)

            game_id = str(uuid.uuid4())
            game_state = GameState(
                game_id=game_id,
                characters=game_characters,
                secret_character=secret_character,
                attempts=0,
            )

            self.games[game_id] = game_state
            logger.info(f"Created new game with ID: {game_id}")
            return game_id, game_characters, secret_character
        except Exception as e:
            logger.error(f"Failed to create game: {str(e)}")
            raise

    def _validate_game_state(self, game: Optional[GameState]) -> GameState:
        """Validate game state and handle common error cases.

        Args:
            game: GameState to validate

        Returns:
            Validated GameState

        Raises:
            GameNotFoundError: If game doesn't exist
            GameOverError: If max attempts reached
        """
        if not game:
            raise GameNotFoundError("Game not found")

        if game.attempts >= self.MAX_ATTEMPTS:
            raise GameOverError("Game Over - No more attempts left")

        return game

    def process_question(self, game_id: str, question: str) -> Tuple[str, int]:
        """Process a player's question.

        Args:
            game_id: ID of the game session
            question: Question asked by the player

        Returns:
            Tuple of (answer, remaining_attempts)
        """
        try:
            game = self._validate_game_state(self.get_game(game_id))

            question = question.strip().lower()
            if not question:
                return "Invalid question", self.MAX_ATTEMPTS - game.attempts

            game.attempts += 1
            remaining = self.MAX_ATTEMPTS - game.attempts

            ai_player = AIPlayer(game.secret_character, self.config)
            answer = ai_player.answer_question(question)

            logger.info(
                f"Game {game_id}: Question processed, {remaining} attempts remaining"
            )
            return answer, remaining

        except (GameNotFoundError, GameOverError) as e:
            logger.warning(f"Game {game_id}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error processing question: {str(e)}")
            raise

    def get_game(self, game_id: str) -> Optional[GameState]:
        """Get the game state for a given game ID."""
        return self.games.get(game_id)

    def process_guess(
        self, game_id: str, character_name: str
    ) -> Optional[Tuple[bool, str, int]]:
        """Process a character guess and return (is_correct, message, remaining_attempts)"""
        try:
            game = self._validate_game_state(self.get_game(game_id))

            game.attempts += 1
            remaining = self.MAX_ATTEMPTS - game.attempts

            is_correct = game.secret_character.name.lower() == character_name.lower()

            message = (
                f"Félicitations ! Vous avez trouvé en {game.attempts} tentatives !"
                if is_correct
                else "Désolé, ce n'est pas le bon personnage. Continuez à chercher !"
            )

            logger.info(
                f"Game {game_id}: Guess processed, correct: {is_correct}, {remaining} attempts remaining"
            )
            return is_correct, message, remaining

        except (GameNotFoundError, GameOverError) as e:
            logger.warning(f"Game {game_id}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error processing guess: {str(e)}")
            raise
