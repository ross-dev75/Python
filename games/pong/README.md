# Pong

## What it does

Two-player Pong in an 800×600 window. Left player uses W/S; right player uses Up/Down. First to let the ball out three times loses.

## Key concepts

- OOP with `Paddle`, `Ball`, and `Scoreboard` classes
- Ball speed increases on each successful paddle hit
- Collision detection using turtle distance and x-coordinate thresholds

## How it works

`Ball` tracks x/y move vectors and flips them on wall or paddle contact. `speed_up()` multiplies the sleep timer by 0.9 after each hit. The `out_of_bounds_limit` counter tracks how many times each side has let the ball escape; when it hits zero the game ends.

## How to run

```
$ python main.py
```
