import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        self.label = tk.Label(self.master, text="Enter time (in seconds):")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(self.master, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack(pady=10)
        
        self.remaining_label = tk.Label(self.master, text="")
        self.remaining_label.pack(pady=10)
        
        self.timer_running = False
        
    def start_countdown(self):
        if not self.timer_running:
            try:
                seconds = int(self.entry.get())
                if seconds <= 0:
                    messagebox.showerror("Error", "Please enter a positive integer.")
                    return
                
                self.end_time = datetime.now() + timedelta(seconds=seconds)
                self.update_remaining_time()
                self.timer_running = True
                self.master.after(1000, self.update_remaining_time)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number of seconds.")
    
    def update_remaining_time(self):
        if self.timer_running:
            remaining = self.end_time - datetime.now()
            if remaining <= timedelta(seconds=0):
                self.remaining_label.config(text="Time's up!")
                self.timer_running = False
            else:
                self.remaining_label.config(text=f"Time remaining: {remaining}")
                self.master.after(1000, self.update_remaining_time)

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
