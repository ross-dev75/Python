# Quiz Game

## What it does

A terminal true/false quiz. Asks 10 questions drawn from Open Trivia DB data, tracks score, and prints it after each answer.

## Key concepts

- OOP with `Question` and `QuizBrain` classes
- Separating data (`data.py`) from model (`question_model.py`) from game logic (`quiz_brain.py`)

## How it works

`main.py` builds a question bank from the JSON data, hands it to `QuizBrain`, and loops `next_question()` until the bank is empty. Scoring and answer-checking live entirely in `QuizBrain`.

## How to run

```
$ python main.py
```
