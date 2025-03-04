"""
Main application entry point for the AI Who Is game.
Configures FastAPI server and starts the application.
"""

import logging
from typing import NoReturn

import uvicorn
from fastapi import FastAPI
from api.routes import router
from utils.config import Settings, get_settings

logger = logging.getLogger(__name__)

def create_app(settings: Settings) -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.version,
        docs_url="/docs",
    )
    app.include_router(router)
    return app

def start_server(app: FastAPI, settings: Settings) -> NoReturn:
    """Start the uvicorn server with error handling."""
    try:
        logger.info(f"Starting server on {settings.api_host}:{settings.api_port}")
        uvicorn.run(
            app,
            host=settings.api_host,
            port=settings.api_port,
            reload=settings.debug,
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise


if __name__ == "__main__":
    settings = get_settings()
    app = create_app(settings)
    start_server(app, settings)
