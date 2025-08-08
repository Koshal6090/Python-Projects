import tkinter as tk
from tkinter import messagebox

# Global variables to keep track of timer state
paused = False
current_time_left = 0

def start_timer():
    global current_time_left, paused
    try:
        current_time_left = int(entry.get())
        paused = False
        countdown()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of seconds.")

def pause_resume_timer():
    global paused
    paused = not paused
    if not paused:
        countdown()
    pause_button.config(text="Pause" if not paused else "Resume")

def countdown():
    global current_time_left
    if current_time_left > 0:
        if not paused:
            mins = current_time_left // 60
            secs = current_time_left % 60
            time_display = f"{mins:02}:{secs:02}"
            label.config(text=time_display)
            current_time_left -= 1
            root.after(1000, countdown)
    else:
        if not paused:
            label.config(text="00:00")
            messagebox.showinfo("Time's up!", "Countdown finished!")

# GUI setup
root = tk.Tk()
root.title("Countdown Timer with Pause/Resume")
root.geometry("300x200")

label = tk.Label(root, text="00:00", font=("Helvetica", 48))
label.pack(pady=10)

entry = tk.Entry(root, justify='center', font=("Helvetica", 14))
entry.pack(pady=5)
entry.insert(0, "10")  # Default time

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_resume_timer)
pause_button.pack(pady=5)

root.mainloop()
