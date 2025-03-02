# GitHub Copilot Instructions

## Project Overview
AI Who Is: A game where you play against an artificial intelligence (AI). The AI chooses a mystery character and you must ask questions to discover the AI's mystery character.

## Instructions
- Keep the `changelog.md` file updated with developed features
- Ensure each feature is documented in the `README.md`
- Clearly explain the reasoning behind each feature implementation
- Ask questions if instructions are unclear

## Conventions

### Coding Style
- Use Python type hints
- Document functions with docstrings
- Use Pydantic for data models
- Use logging instead of print statements
- Follow PEP 8 conventions

### Error Handling
- Use try/except blocks with specific exceptions
- Log errors with appropriate level (error, warning, info)
- Return Optional types for functions that might fail

## Project Structure

```
ai-who-is/
├── src/
│   ├── models/            # Data models using Pydantic
│   │   ├── character.py   # Character model definitions
│   │   └── game.py       # Game state models
│   ├── services/          # Business logic services
│   │   ├── ai_service.py  # AI/LLM integration
│   │   ├── game_service.py# Game mechanics
│   │   └── db_service.py  # Data persistence
│   ├── utils/            # Utility functions
│   │   ├── logger.py     # Logging configuration
│   │   └── config.py     # App configuration
│   ├── api/             # API endpoints (if needed)
│   │   └── routes.py    # API route definitions
│   └── __init__.py
├── tests/
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── conftest.py     # Test configurations
├── data/
│   ├── characters/      # Character data files
│   └── config/         # Configuration files
├── logs/               # Application logs
└── docs/              # Documentation
```

## Features

All instructions are in the `docs/roadmap-console.md` file. Please refer to this file for the project roadmap.

Check the roadmap for the next feature to implement. If you have any questions, please ask.