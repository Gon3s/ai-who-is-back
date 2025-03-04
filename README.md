# AI Who Is

A fun guessing game where you play against an AI. Ask yes/no questions to discover the mystery character chosen by the AI!

## 🌟 Features

- Interactive question-and-answer gameplay
- AI-powered responses using Groq LLM
- Character database with various attributes
- Logging system for game progression
- Limited attempts for added challenge

## 📂 Project Structure

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

## 📋 Prerequisites

- Python 3.9+
- A Groq API key (get it from [Groq Console](https://console.groq.com/))

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/Gon3s/ai-who-is-back.git
cd ai-who-is-back
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```

## ⚙️ Configuration

Edit the `.env` file with your settings:

```env
AIWHO_API_KEY=your_groq_api_key_here
```

Optional settings:
- `AIWHO_MODEL_NAME`: LLM model name (default: llama-3.1-8b-instant)
- `AIWHO_TEMPERATURE`: Generation temperature (default: 0.3)
- `AIWHO_MAX_TOKENS`: Max response tokens (default: 50)

## 🎮 How to Play

1. Start the game
```bash
python -m src.game
```

2. The game will display available characters and their attributes
3. Ask yes/no questions about the mystery character
4. Try to guess who it is within 20 attempts!

## 🧪 Running Tests

```bash
pytest tests/
```

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
- Original "Guess Who?" board game for inspiration
