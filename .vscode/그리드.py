from ast import Num
from optparse import check_builtin
from tkinter import *
from traceback import print_tb
import tkinter.messagebox as msgbox
from matplotlib.pyplot import text

root = Tk()

root.title("Python GUI")
root.geometry("600x400")


Button(root, text='F16', width=10, height=3).grid(row=0, column=0)
Button(root, text='F17', width=10, height=3).grid(row=0, column=1)
Button(root, text='F18', width=10, height=3).grid(row=0, column=2)
Button(root, text='F19', width=10, height=3).grid(row=0, column=3)

Button(root, text='clear', width=10, height=3).grid(row=1, column=0)
Button(root, text='=', width=10, height=3).grid(row=1, column=1)
Button(root, text='/', width=10, height=3).grid(row=1, column=2)
Button(root, text='*', width=10, height=3).grid(row=1, column=3)

Button(root, text='7', width=10, height=3).grid(row=2, column=0)
Button(root, text='8', width=10, height=3).grid(row=2, column=1)
Button(root, text='9', width=10, height=3).grid(row=2, column=2)
Button(root, text='-', width=10, height=3).grid(row=2, column=3)

Button(root, text='4', width=10, height=3).grid(row=3, column=0)
Button(root, text='5', width=10, height=3).grid(row=3, column=1)
Button(root, text='6', width=10, height=3).grid(row=3, column=2)
Button(root, text='+', width=10, height=3).grid(row=3, column=3)

Button(root, text='1', width=10, height=3).grid(row=4, column=0)
Button(root, text='2', width=10, height=3).grid(row=4, column=1)
Button(root, text='3', width=10, height=3).grid(row=4, column=2)
Button(root, text='enter', width=10, height=3).grid(row=4, column=3)

numEdit = Entry(root, width=40)
numEdit.insert(END, "숫자를 입력하세요")
numEdit.grid(row=6, column=0, columnspan=4)


root.mainloop()
