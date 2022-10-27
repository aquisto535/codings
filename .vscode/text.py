from cProfile import label
from tkinter import *
from turtle import color

root = Tk()
root.title("Python GUI")
root.geometry("800x640+500+100")

txt = Text(root, width=40, height=20)
txt.insert(END, "글자를 입력하세요")
txt.pack()


root.mainloop()
