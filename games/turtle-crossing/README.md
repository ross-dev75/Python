# Turtle Crossing

## What it does

Frogger-style crossing game. Guide the turtle from the bottom to the top without getting hit by cars. Each successful crossing increases car speed.

## Key concepts

- OOP with `Player`, `CarManager`, and `Scoreboard` classes
- Random car spawning with level-based speed scaling
- Collision detection via turtle distance threshold

## How it works

`CarManager` randomly spawns cars (1-in-6 chance each tick) at the right edge and moves them left. On a successful crossing, `level_up()` increases `starting_move_distance` by 10. A car collision ends the game.

## How to run

```
$ python main.py
```
