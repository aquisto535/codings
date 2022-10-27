from cProfile import label
from tkinter import *
from turtle import color

root = Tk()
root.title("Python GUI")
root.geometry("800x640+500+100")
#root.resizable(False, False)

photo1 = PhotoImage(file="test.png")
#label = Label(root, text="누구인가? 누가 소리를 내었어?")
label = Label(root, image=photo1)
label.pack()


def btncmd():
    print('좋아요를 꾹 눌러주세요')


photo2 = PhotoImage(file="sea.png")
btn = Button(root, image=photo2, command=btncmd)
btn.pack()

root.mainloop()  # 이벤트를 체크하기 위해서 mainloop를 돈다.
