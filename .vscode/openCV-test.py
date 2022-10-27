from csv import writer
import cv2

'''
# 이미지 읽기

img1 = cv2.imread('sea.png', cv2.IMREAD_COLOR)


# 이미지 화면에 표시하기

cv2.imshow('sea color', img1)
cv2.waitKey(0)


# 이미지 윈도우 삭제

cv2.destroyAllWindows()
cv2.imwrite('sea.jpg', img1)
'''

# 카메라 영상 처리

cap = cv2.VideoCapture(0)  # default camera
# cap = cv2.VideoCapture('test.mp4') 동영상 파일에서 읽기

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("size : {0} x {1}".format(width, height))

# 영상 저장을 위한 videowriter 인스턴스 생성

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("cam.avi", fourcc, 24, (int(width), int(height)))

while cap.isOpened():
    # 카메라 프레임 읽기
    sucess, frame = cap.read()
    if sucess:
        # 프레임 출력
        cv2.imshow('Camera Window', frame)
        writer.write(frame)  # 프레임 저장

        # esc 키를 누르면 종료
        key = cv2.waitKey(1)
        if (key == 27):
            break

cap.release()
writer.release()
cv2.destroyAllWindows()
