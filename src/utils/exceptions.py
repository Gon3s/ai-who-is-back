class GameError(Exception):
    """Base class for game-related exceptions."""

    pass


class GameNotFoundError(GameError):
    """Raised when a game session is not found."""

    pass


class GameOverError(GameError):
    """Raised when game is over (max attempts reached)."""

    pass
