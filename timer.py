

import tkinter as tk
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")
        self.master.geometry("300x150")
        
        self.label = tk.Label(self.master, text="Enter time in seconds:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)
        
        self.timer_label = tk.Label(self.master, font=("Helvetica", 24), text="00:00:00")
        self.timer_label.pack(pady=10)
        
    def start_timer(self):
        try:
            set_timer = int(self.entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer")
            return
        
        for i in range(set_timer,0,-1):
            seconds = i%60
            minutes = int(i/60)%60
            hours   = int(i/3600)
            self.timer_label.config(text="{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))
            self.master.update()
            time.sleep(1)
        
        tk.messagebox.showinfo("Time's Up!", "Your timer has ended!")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
