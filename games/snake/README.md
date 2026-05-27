# Snake

## What it does

Classic Snake game in a 600×600 window. Eat food to grow; avoid walls and your own tail. Difficulty selection at launch. Low scores are met with commentary.

## Key concepts

- OOP with `Snake`, `Food`, and `Scoreboard` classes (originally four files, combined into one)
- Turtle graphics for game rendering
- Collision detection via coordinate distance checks

## How it works

The snake is a list of `Turtle` squares. On each tick, segments shift forward by copying the position of the segment ahead of them, then the head moves. Food collision triggers `grow()`, which appends a new segment at the tail's last position. Wall and self-collision end the game.

## How to run

```
$ python snake_game.py
```

Select `insane` at the prompt for a faster game.
