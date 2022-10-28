from optparse import check_builtin
from tkinter import *
from traceback import print_tb
import tkinter.messagebox as msgbox
from matplotlib.pyplot import text

root = Tk()

root.title("Python GUI")
root.geometry("800x640+500+100")


def newFile():
    print('파일을 새로 만듭니다.')


myMenu = Menu(root)
menu_file = Menu(myMenu, tearoff=0)
menu_file.add_command(label="New File", command=newFile)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_command(label="Save File")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

myMenu.add_cascade(label="File", menu=menu_file)
myMenu.add_cascade(label="Edit")


def showminimap():
    msgbox.showwarning("알림", "미니맵을 보여 줍니다.")


def showmaximap():
    msgbox.showerror("알림", "맥스맵을 보여줍니다.")


menu_view = Menu(myMenu, tearoff=0)
menu_view.add_checkbutton(label="Show minimap", command=showminimap)
menu_view.add_checkbutton(label="Show maxmap", command=showmaximap)

myMenu.add_cascade(label="View", menu=menu_view)

root.config(menu=myMenu)

root.mainloop()
