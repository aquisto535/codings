from optparse import check_builtin
from tkinter import *

import time
import tkinter.ttk as ttk

from matplotlib.pyplot import text
from numpy import deg2rad
from soupsieve import select

root = Tk()

root.title("Python GUI")
root.geometry("800x640+500+100")

p_var = DoubleVar()

Progressbar1 = ttk.Progressbar(
    root, maximum=100, length=400, mode="determinate", variable=p_var)
Progressbar1.pack()

Progressbar2 = ttk.Progressbar(root, maximum=100, mode="indeterminate")
Progressbar2.pack()


def btnStart():
    for i in range(1, 101):
        time.sleep(0.01)
        p_var.set(i)
        Progressbar1.update()
        print(p_var.get())


Button(root, text="전송", command=btnStart).pack()


def btnStop():
    Progressbar1.stop()
    Progressbar2.stop()


Button(root, text="정지", command=btnStop).pack()

root.mainloop()
