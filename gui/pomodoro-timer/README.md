# Pomodoro Timer

## What it does

A Pomodoro timer that cycles automatically through four focus blocks and their breaks (4×25-minute focus sessions, 3×5-minute short breaks, 1×20-minute long break). Raises the window and plays a native Windows audio alert at each transition.

## Key concepts

- `window.after()` for non-blocking countdown ticks
- Explicit `after_cancel()` on pause to prevent timer acceleration on resume
- `winsound.MessageBeep` for native audio (Windows only)

## How it works

`SESSIONS` is a list of `(name, minutes)` tuples. `countdown()` decrements `time_left` each second via `window.after(1000, countdown)`. When a session reaches zero, the index advances and the next session starts immediately. Pause cancels the pending `after` callback and stores the ID so it can be cleanly torn down.

## How to run

Requires `Pillow` for the background image. Replace `background.jpg` in the script with a local image path before running.

```
$ pip install Pillow
$ python pomodoro.py
```
