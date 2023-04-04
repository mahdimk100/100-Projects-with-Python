import tkinter as tk
from datetime import datetime

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title('Timer')
        self.time_label = tk.Label(self.master, font=('Helvetica', 48))
        self.time_label.pack(pady=20)
        self.start_button = tk.Button(self.master, text='Start', command=self.start_timer)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.master, text='Stop', command=self.stop_timer)
        self.stop_button.pack(pady=10)
        self.reset_button = tk.Button(self.master, text='Reset', command=self.reset_timer)
        self.reset_button.pack(pady=10)
        self.timer_running = False
        self.start_time = None
        
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = datetime.now()
            self.update_timer()
            
            
    def stop_timer(self):
        self.timer_running = False
        
    def reset_timer(self):
        self.timer_running = False
        self.start_time = None
        self.time_label.config(text='00:00:00')
        
    def update_timer(self):
        if self.timer_running:
            elapsed_time = datetime.now() - self.start_time
            timer_str = str(elapsed_time).split('.')[0]
            self.time_label.config(text=timer_str)
            self.master.after(1000, self.update_timer)

root = tk.Tk()
timer = Timer(root)
root.mainloop()