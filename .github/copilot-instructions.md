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

### Commits
- Use gitmoji in commit messages
- Follow conventional commits format
- Keep commits focused and atomic