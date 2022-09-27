import os
srcfile = "SleepAway.mp3"

if os.path.exists(srcfile):
    sfp = open(srcfile, 'rb')

    # 음원 데이터를 읽어오기
    sfp.seek(-128, 2)
    tdata = sfp.read(128)

    title = tdata[3:33].decode()
    print("제목 : " + title)

    artist = tdata[33:63].decode()
    print("음악가 : " + artist)

    mdate = tdata[93:97].decode()
    print("출시년도 : " + mdate)

    etc = tdata[97:127].decode()
    print("기타정보 : " + etc)

    sfp.close()

    print('음악 파일 정보를 정상적으로 출력하였습니다')

else:
    print(srcfile + '파일은 존재하지 않습니다')
