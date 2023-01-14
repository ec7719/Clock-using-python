import tkinter as tk
from tkinter.ttk import *
from tkinter import *

from time import strftim
root=tk.Tk()
root.title("Clock")
def clock():
    disp=strftime('%H:%M:%S %p')
    label.config(text=disp)
    label.after(1000,clock)
label=Label(root,font=('italic',180),background='white',foreground='black')
label.pack(anchor='center')
clock()
root.mainloop()
