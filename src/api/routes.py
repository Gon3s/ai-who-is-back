from fastapi import APIRouter, HTTPException, status
from models.game import (
    GameResponse,
    QuestionRequest,
    QuestionResponse,
    GuessRequest,
    GuessResponse,
)
from services.game_service import GameService, GameNotFoundError
from utils.logger import get_app_logger

router = APIRouter()
game_service = GameService()
logger = get_app_logger(__name__)

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """
    Health check endpoint to verify API availability
    Returns:
        dict: Status message indicating health state
    """
    return {"status": "healthy"}

@router.post(
    "/game/init", response_model=GameResponse, status_code=status.HTTP_201_CREATED
)
async def initialize_game():
    """
    Initialize a new game session
    Returns:
        GameResponse: Contains game_id and available characters
    Raises:
        HTTPException: If game creation fails
    """
    try:
        game_id, characters, _ = game_service.create_game()
        logger.info(f"New game created with ID: {game_id}")
        return GameResponse(game_id=game_id, characters=characters)
    except Exception as e:
        logger.error(f"Failed to create game: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create new game",
        )


@router.post("/game/question", response_model=QuestionResponse)
async def ask_question(question_req: QuestionRequest):
    """
    Process a game question
    Args:
        question_req (QuestionRequest): Contains game_id and question
    Returns:
        QuestionResponse: Answer and remaining attempts
    Raises:
        HTTPException: If game not found or invalid request
    """
    try:
        if not question_req.question.strip():
            raise ValueError("Question cannot be empty")

        result = game_service.process_question(
            question_req.game_id, question_req.question
        )
        if result is None:
            raise GameNotFoundError(f"Game {question_req.game_id} not found")

        answer, remaining = result
        logger.info(
            f"Question processed for game {question_req.game_id}. Remaining attempts: {remaining}"
        )
        return QuestionResponse(answer=answer, remaining_attempts=remaining)

    except GameNotFoundError as e:
        logger.warning(str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        logger.warning(str(e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process question",
        )

@router.post("/game/guess", response_model=GuessResponse)
async def make_guess(guess_req: GuessRequest):
    """
    Process a character guess
    Args:
        guess_req (GuessRequest): Contains game_id and character_name
    Returns:
        GuessResponse: Result of the guess and remaining attempts
    Raises:
        HTTPException: If game not found or invalid request
    """
    try:
        if not guess_req.character_name.strip():
            raise ValueError("Character name cannot be empty")

        result = game_service.process_guess(guess_req.game_id, guess_req.character_name)
        if result is None:
            raise GameNotFoundError(f"Game {guess_req.game_id} not found")

        is_correct, message, remaining = result
        logger.info(
            f"Guess processed for game {guess_req.game_id}. Correct: {is_correct}, Remaining attempts: {remaining}"
        )
        return GuessResponse(
            is_correct=is_correct, message=message, remaining_attempts=remaining
        )

    except GameNotFoundError as e:
        logger.warning(str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        logger.warning(str(e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing guess: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process guess",
        )
