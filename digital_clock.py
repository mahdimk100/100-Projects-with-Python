from tkinter import *
import time

root = Tk()
root.title('Digital Clock')
root.geometry('300x100')

clock_label = Label(root, font=('Arial', 30, 'bold'),
                    bg='black', fg='white', bd=30)

clock_label.pack(fill=BOTH, expand=1)

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)
    
update_clock()
root.mainloop()