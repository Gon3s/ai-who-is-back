import logging
import os
import sys
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str,
    log_file: Optional[str] = None,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """
    Configure and return a logger with the specified settings.

    Args:
        name: Name of the logger (typically __name__ from the calling module)
        log_file: Path to log file (default: None = logs to console only)
        log_format: Format string for log messages

    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(log_format)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    # Create file handler if log_file is specified
    if log_file:
        # Create directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        Path(log_dir).mkdir(parents=True, exist_ok=True)

        # Create file handler
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    return logger


def get_app_logger(module_name: str, logs_dir: str = "logs") -> logging.Logger:
    """
    Configure and return a logger with the specified settings.

    Args:
        name: Name of the logger (typically __name__ from the calling module)
        log_file: Path to log file (default: None = logs to console only)
        log_format: Format string for log messages

    Returns:
        Configured logger instance
    """
    log_file = os.path.join(logs_dir, "api.log")

    return setup_logger(
        module_name,
        log_file=log_file,
        log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
