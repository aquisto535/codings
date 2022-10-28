from optparse import check_builtin
from tkinter import *

import tkinter.ttk as ttk

from matplotlib.pyplot import text
from soupsieve import select

root = Tk()

root.title("Python GUI")
root.geometry("800x640+500+100")

dateVal = [str(i) + '일' for i in range(1, 32)]

combobox = ttk.Combobox(root, height=10, values=dateVal, state="readonly")
combobox.current(0)
combobox.pack()
combobox.set("통장은 거들뿐")


def selectDate():
    print(combobox.get())


Button(root, text="날짜 선택", command=selectDate).pack()


root.mainloop()
