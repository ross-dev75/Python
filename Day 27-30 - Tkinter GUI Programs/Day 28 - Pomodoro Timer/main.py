from tkinter import *
from PIL import Image, ImageTk
import winsound

# Define the full loop sequence: (Session Name, Duration in Minutes)
SESSIONS = [
    ("Focus 1/4", 25), ("Short Break", 5),
    ("Focus 2/4", 25), ("Short Break", 5),
    ("Focus 3/4", 25), ("Short Break", 5),
    ("Focus 4/4", 25), ("Long Break", 20)
]

current_session_index = 0
time_left = SESSIONS[current_session_index][1] * 60

is_running = True
timer_id = None


def countdown():
    global time_left, is_running, timer_id, current_session_index

    if not is_running:
        return

    minutes = time_left // 60
    seconds = time_left % 60

    counter_label.config(text=f"{minutes:02}:{seconds:02}")

    if time_left > 0:
        time_left -= 1
        timer_id = window.after(1000, countdown)
    else:
        # 1. Trigger window pop and native audio alert
        trigger_alert()

        # 2. Advance to the next scheduled session block
        current_session_index = (current_session_index + 1) % len(SESSIONS)

        # 3. Pull fresh session variables
        session_name, minutes_duration = SESSIONS[current_session_index]
        time_left = minutes_duration * 60

        # 4. Instant UI Text Updates
        status_label.config(text=session_name)
        counter_label.config(text=f"{minutes_duration:02}:00")

        # 5. Cadence Fix: Subtract first second immediately to bypass transition lag
        time_left -= 1
        timer_id = window.after(1000, countdown)


def trigger_alert():
    # Force application window above all other background applications
    window.attributes("-topmost", True)
    window.attributes("-topmost", False)
    window.lift()
    # Play clean native Windows Asterisk chime
    winsound.MessageBeep(winsound.MB_ICONASTERISK)


def toggle_pause():
    global is_running, timer_id
    if is_running:
        is_running = False
        pause_button.config(text="Resume")
        # Explicitly tear up the event ticket to eliminate multi-loop speed acceleration bugs
        if timer_id is not None:
            window.after_cancel(timer_id)
            timer_id = None
    else:
        is_running = True
        pause_button.config(text="Pause")
        countdown()


def play_test_sound():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)


# --- Window Initialization ---
window = Tk()
window.title("Pomodoro Timer")
window.geometry("400x400")

# --- Asset Management ---
image = Image.open(r"C:\Users\jukof\Pictures\sisyphus_unbothered.jpg")
image = image.resize((400, 400))
photo = ImageTk.PhotoImage(image)

image_label = Label(window, image=photo)
image_label.place(x=0, y=0)

# --- UI Element Layouts ---
status_label = Label(
    window,
    text=SESSIONS[current_session_index][0],
    font=("Arial", 16, "bold"),
    bg="black",
    fg="#deaa88"
)
status_label.place(relx=0.5, rely=0.63, anchor="center")

counter_label = Label(
    window,
    text="25:00",
    font=("Arial", 26, "bold"),
    bg="black",
    fg="white"
)
counter_label.place(relx=0.5, rely=0.74, anchor="center")

pause_button = Button(
    window,
    text="Pause",
    font=("Arial", 12, "bold"),
    command=toggle_pause,
    bg="white",
    fg="black",
    padx=10,
    pady=5
)
pause_button.place(relx=0.35, rely=0.88, anchor="center")

sound_button = Button(
    window,
    text="Beep",
    font=("Arial", 12, "bold"),
    command=play_test_sound,
    bg="white",
    fg="black",
    padx=10,
    pady=5
)
sound_button.place(relx=0.65, rely=0.88, anchor="center")

# Run initial execution loop
countdown()

window.mainloop()