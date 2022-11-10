import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound
import os
from tkinter import *
import tkinter.messagebox as msgbox

# os.path = 일반적인 경로명 조작,  dirname(__file__) = 현재 폴더 경로
audio_file = os.path.dirname(__file__) + '\\qrbarcode_beep.mp3'
image_file = os.path.dirname(__file__) + '\\qrbarcode_image.png'
txt_file = os.path.dirname(__file__) + '\\qrbarcode_data.txt'

used_codes = []
data_list = []

try:
    f = open(txt_file, "r", encoding="utf8")
    data_list = f.readlines()
except FileNotFoundError:
    pass
else:
    f.close()

cap = cv2.VideoCapture(0)

# 가로와 세로의 크기 설정
cap.set(3, 640)
cap.set(4, 480)

for i in data_list:
    used_codes.append(i.rstrip('\n'))

while True:
    success, frame = cap.read()
    key = cv2.waitKey(1)

    if key == 27:
        break
    for code in pyzbar.decode(frame):
        cv2.imwrite(image_file, frame)
        my_code = code.data.decode('utf-8')
        if my_code not in used_codes:
            msgbox.showinfo('알림', "인식이 되었습니다")
            playsound(audio_file)
            used_codes.append(my_code)

            f2 = open(txt_file, "a", encoding="utf8")
            f2.write(my_code+'\n')
            f2.close()
            print(key)
        elif my_code in used_codes:
            msgbox.showerror('에러', '이미 인식된 코드입니다!!!')

        else:
            pass

    cv2.imshow('QRcode Barcode Scan', frame)


cap.release()
cv2.destroyAllWindows()
