from tkinter import *
from turtle import color

root = Tk()
root.title("Python GUI")
root.geometry("800x640+500+100")
#root.resizable(False, False)

btn1 = Button(root, text="버튼인가?")
btn1.pack()

btn2 = Button(root, padx=20, pady=20, text="아무튼")
btn2.pack()

btn3 = Button(root, width=10, height=5, text="튼튼", fg='white', bg='red')
btn3.pack()


root.mainloop()  # 이벤트를 체크하기 위해서 mainloop를 돈다.
