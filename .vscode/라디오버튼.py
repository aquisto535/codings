from optparse import check_builtin
from tkinter import *
from traceback import print_tb

from matplotlib.pyplot import text

root = Tk()

root.title("Python GUI")
root.geometry("800x640+500+100")

Label(root, text="햄버거를 선택하세요").pack()

burger_var = StringVar()

btn_burger1 = Radiobutton(
    root, text="불고기 버거", value='불고기 버거', variable='burger_var')
btn_burger2 = Radiobutton(
    root, text="치즈 버거", value='치즈 버거', variable='burger_var')
btn_burger3 = Radiobutton(
    root, text="치킨 버거", value='치킨 버거', variable='burger_var')

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

btn_burger1.select()


def order():
    print(burger_var.get() + ' 를 선택하였습니다.')


Button(root, text="주문", command=order).pack()

root.mainloop()
