# US States Quiz

## What it does

Geography quiz displayed on a blank US map. Type a state name; if correct it gets labeled at its coordinates on the map. On exit, saves unguessed states to `states_to_learn.csv`.

## Key concepts

- pandas for CSV reading and filtered output
- turtle for GUI and text rendering over a `.gif` background image
- Combining data lookup with real-time graphical feedback

## How it works

`50_states.csv` contains each state's name and x/y coordinates on the map image. Each correct guess looks up the state's row in the DataFrame and uses `turtle.goto(x, y)` + `write()` to label it. On exit, pandas filters out the guessed states and saves the remainder.

## How to run

```
$ python main.py
```
