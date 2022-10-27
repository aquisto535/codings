from cProfile import label
from tkinter import *
from turtle import color

root = Tk()
root.title("Python GUI")
root.geometry("800x640+500+100")
#root.resizable(False, False)

label1 = Label(root, text="최선을 다하자")
label1.pack()

def change():
    #label1.config(text="최선을 다하지 말자")
    global photo1
    photo1 = PhotoImage(file="logo.png")
    label1.config(image=photo1)

photo2 = PhotoImage(file="sea.png")
btn = Button(root, image=photo2, command=change)
btn.pack()

root.mainloop()  # 이벤트를 체크하기 위해서 mainloop를 돈다.
