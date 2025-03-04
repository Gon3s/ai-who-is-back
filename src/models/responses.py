from enum import Enum


class ValidResponse(Enum):
    """Enum representing the possible responses from the AI."""

    YES = "Oui"
    NO = "Non"
    UNKNOWN = "Je ne peux pas répondre"
