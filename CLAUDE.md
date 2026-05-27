# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal collection of Python exercises and small projects from self-paced study, organized by category. This is an honest learning artifact, not a portfolio — original projects live in separate repos.

## Structure

```
fundamentals/        # Standalone scripts: control flow, data structures, early projects
oop/
└── coffee-maker/    # OOP coffee machine (CoffeeMaker, MoneyMachine, Menu classes)
turtle-graphics/
├── spirograph/
├── color-palette/
├── etch-a-sketch/
└── turtle-race/
games/
├── quiz/            # OOP true/false quiz (QuizBrain, Question)
├── snake/           # Snake with OOP + difficulty select (single file)
├── pong/            # Two-player Pong (Ball, Paddle, Scoreboard)
├── turtle-crossing/ # Frogger clone (Player, CarManager, Scoreboard)
└── states-quiz/     # US states map quiz using pandas + turtle
data/
└── mail-merge/      # Letter generator from template + name list
gui/
├── tkinter-widgets/ # Widget reference and miles-to-km converter
├── pomodoro-timer/  # Pomodoro timer with audio alerts (Windows)
└── password-manager/# Encrypted credential vault (PBKDF2 + Fernet)
```

## Naming conventions

- Directory names: `lowercase-with-hyphens`
- Python files: `snake_case.py`
- No "Day X" prefixes anywhere

## Running files

Most scripts run directly with `python <file>.py`. Multi-file projects use `main.py` or a descriptively named entry point (e.g., `snake_game.py`, `password_manager.py`).

Notable dependencies:
- `gui/password-manager/`: `pip install cryptography pyperclip`
- `gui/pomodoro-timer/`: `pip install Pillow` — also requires setting a local image path in `pomodoro.py`
- `turtle-graphics/color-palette/color_extractor.py`: `pip install colorgram.py`
- `games/states-quiz/`: `pip install pandas`

## Known incomplete files

`fundamentals/hangman.py` imports `hangman_words` and `hangman_art` (not committed).
`fundamentals/higher_lower.py` imports `game_data` and `art` (not committed).
These won't run without those modules.

## What NOT to do

- No force-push, no `filter-repo`, no history rewriting
- Don't commit `data.enc` (gitignored) or any credential files
- Don't pre-create empty folders for future course days
