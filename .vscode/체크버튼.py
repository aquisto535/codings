from optparse import check_builtin
from tkinter import *

from matplotlib.pyplot import text

root = Tk()

root.title("Python GUI")
root.geometry("800x640+500+100")

chClick = IntVar()
chClick2 = IntVar()

chkbox1 = Checkbutton(root, text="일주일 동안 보지 않기")
chkbox1.pack()

chkbox2 = Checkbutton(root, text="오늘 하루 그만보기")
chkbox2.pack()


def getCheck():
    print("체크 상태 : ", chClick.get())


Button(root, text="확인", command=getCheck).pack()


chkbox1.select()
chkbox2.deselect()

root.mainloop()
