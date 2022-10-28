from optparse import check_builtin
from tkinter import *
from traceback import print_tb
import tkinter.messagebox as msgbox
from matplotlib.pyplot import text

root = Tk()

root.title("Python GUI")
root.geometry("800x640+500+100")


def info():
    msgbox.showinfo('알림', "정상적으로 예매가 완료되었습니다")


def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다')


def error():
    msgbox.showerror('에러', '결제 오류가 발생하였습니다')


def okcancel():
    result = msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

    if result == 1:
        msgbox.showinfo('알림', '예매가 완료되었습니다.')
    elif result == 0:
        msgbox.showinfo('알림', '예매가 취소되었습니다.')


Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()
Button(root, command=okcancel, text='확인/취소').pack()

root.mainloop()
