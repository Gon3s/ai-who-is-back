# AI Who Is

A fun guessing game where you play against an AI. Ask yes/no questions to discover the mystery character chosen by the AI!

## 🌟 Features

- Interactive question-and-answer gameplay
- AI-powered responses using Groq LLM
- Character database with various attributes
- RESTful API for game interaction
- Logging system for game progression
- Limited attempts for added challenge

## 📂 Project Structure

```
ai-who-is/
├── src/
│   ├── models/            # Data models using Pydantic
│   │   ├── character.py   # Character model definitions
│   │   └── game.py        # Game state models
│   ├── services/          # Business logic services
│   │   ├── ai_service.py  # AI/LLM integration
│   │   ├── game_service.py# Game mechanics
│   │   └── db_service.py  # Data persistence
│   ├── utils/             # Utility functions
│   │   ├── logger.py      # Logging configuration
│   │   └── config.py      # App configuration
│   ├── api/               # API endpoints
│   │   └── routes.py      # API route definitions
│   └── __init__.py
├── tests/
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   └── conftest.py       # Test configurations
├── data/
│   ├── characters/       # Character data files
│   └── config/           # Configuration files
├── logs/                 # Application logs
├── _bruno/               # Bruno API client collection
└── docs/                 # Documentation
```

## 📋 Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- A Groq API key (get it from [Groq Console](https://console.groq.com/))
- [Bruno](https://www.usebruno.com/) (optional, for API testing)

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/Gon3s/ai-who-is-back.git
cd ai-who-is-back
```

2. Install uv if you don't have it yet
```bash
# Install with pip
pip install uv

# Or on macOS with Homebrew
brew install uv

# Or on Windows with Scoop
scoop install uv
```

3. Create a virtual environment and install dependencies with uv
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```

## ⚙️ Configuration

Edit the `.env` file with your settings:

```env
# Application Settings
AIWHO_APP_NAME="AI Who Is"
AIWHO_DEBUG=false

# Required: Get your API key from https://console.groq.com/
AIWHO_API_KEY=your_groq_api_key_here
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `AIWHO_APP_NAME` | Application name | "AI Who Is" |
| `AIWHO_DEBUG` | Enable debug mode | false |
| `AIWHO_API_KEY` | **Required:** Your Groq API key | - |
| `AIWHO_MODEL_NAME` | LLM model name | llama-3.1-8b-instant |
| `AIWHO_TEMPERATURE` | Generation temperature (0.0-1.0) | 0.3 |
| `AIWHO_MAX_TOKENS` | Maximum tokens for response | 50 |

**Note:** You must obtain an API key from [Groq Console](https://console.groq.com/) to use this application.

## 🎮 How to Play

### API Server

1. Start the application using uv
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

2. The API will be available at `http://localhost:8000`

3. Use the API endpoints to play:
   - `POST /game/init` - Start a new game
   - `POST /game/question` - Ask a question about the mystery character
   - `POST /game/guess` - Make a guess at the mystery character

## 🔌 Using Bruno API Client

This project includes a [Bruno](https://www.usebruno.com/) API collection to easily interact with the game API.

1. Install Bruno from [usebruno.com](https://www.usebruno.com/downloads)
2. Open Bruno and select "Open Collection"
3. Navigate to the `_bruno` folder in this project
4. Use the available requests:
   - "Init Game" - Starts a new game and stores the game_id
   - "Ask question" - Send a question about the mystery character
   - "Make guess" - Make a guess at who the mystery character is

The collection is set up with environment variables to automatically store the game ID between requests.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m '✨ Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Authors

- Kevin Cuoq - [@Gon3s](https://github.com/Gon3s)

## ✨ Acknowledgments

- Groq for their amazing LLM API
- [uv](https://github.com/astral-sh/uv) for fast Python package management
- Original "Guess Who?" board game for inspiration
