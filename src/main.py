"""
Main application entry point for the AI Who Is game.
Configures FastAPI server and starts the application.
"""

import os
from fastapi import FastAPI, staticfiles
from src.api.routes import router
from src.utils.logger import get_app_logger
from src.utils.config import Settings, get_settings

logger = get_app_logger(__name__)

def create_app(settings: Settings) -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.version,
        docs_url="/api/docs",
    )

    # Include API routes
    app.include_router(router, prefix="/api")

    # Configure static files for serving images
    # The mount path '/images' will be used in URLs
    # The directory path is where the actual image files are stored
    images_directory = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "images"
    )

    # Ensure the images directory exists
    if not os.path.exists(images_directory):
        os.makedirs(images_directory)
        logger.info(f"Created images directory at: {images_directory}")

    # Mount the static files directory
    app.mount(
        "/images",
        staticfiles.StaticFiles(directory=images_directory),
        name="character_images",
    )
    logger.info(f"Mounted static files from {images_directory} to /images")

    return app


# Create the application instance
settings = get_settings()
app = create_app(settings)
