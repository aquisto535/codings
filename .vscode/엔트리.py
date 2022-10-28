from cProfile import label
from msilib.schema import ListBox
from tkinter import *
from turtle import color
from typing import List

from soupsieve import select

root = Tk()
root.title("Python GUI")
root.geometry("800x640+500+100")

Id = Entry(root, width=30)
Id.insert(END, "아이디를 입력하세요")
Id.pack()

pw = Entry(root, width=30)
pw.insert(END, "비밀번호를 입력하세요")
pw.pack()


def login():
    label1.config(text=Id.get())
    label2.config(text=pw.get())


def eraser():
    Id.delete(0, END)
    pw.delete(0, END)


Button(root, text="로그인", command=login).pack()
Button(root, text="삭제", command=eraser).pack()

label1 = Label(root, text="아이디")
label1.pack()

label2 = Label(root, text="비밀번호")
label2.pack()

listbox = Listbox(root, height=5, selectmode='extended')

listbox.insert(0, '파이썬')
listbox.insert(1, 'C#')
listbox.insert(2, '자바스크립트')
listbox.insert(3, '자바')
listbox.insert(4, '몽고DB')
listbox.pack()

Photo = PhotoImage(file="../logo.png")


def lstDelete():
    listbox.delete(END)


Button(root, text='삭제', command=lstDelete).pack()

label3 = Label(root, text="리스트 아이템")
label3.pack()


def lstGetItem():
    print(listbox.get(0, 2))
    label3.config(text=listbox.get(0))


Button(root, text='가져오기', command=lstGetItem).pack()

root.mainloop()
