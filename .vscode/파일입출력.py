import os

# strRead = fp.read() 내용 전체 읽음

'''
한 라인씩 읽을 때
while True:
    strRead = fp.readline()
    if strRead == '':
        break
    print(strRead)

'''


# 텍스트 전체 읽을 때, 전체 문자열 리스트로 리턴
'''
if os.path.exists(fName):
    with open(fName, "r") as fp:

        listRead = fp.readlines()

        for strlist in listRead:
            print(strlist)
else:
    print("%s 파일은 존재하지 않습니다" % fName)

'''

# 데이터 쓰기(데이터 생성)
'''
fName = input('파일 명을 입력하세요')
print()

with open(fName, "w") as fp:
    while True:
        instr = input('데이터 입력 : ')
        if instr == '\q':
            break
        fp.writelines(instr + '\n')

'''
'''
srcFile = input('원본 파일 명을 입력하세요')
destFile = input('대상 파일 명을 입력하세요')
print()

if os.path.exists(srcFile):
    sfp = open(srcFile, 'r')
    dfp = open(destFile, "w")

    slist = sfp.readlines()
    for str in slist:
        dfp.writelines(str)

    sfp.close()
    dfp.close()

    print("복사가 완료하였습니다")
else:
    print("원본파일이 존재하지 않습니다.")

'''

srcfile = 'poem.txt'
destfile = 'poem2.txt'


print()

if os.path.exists(srcfile):
    sfp = open(srcfile, 'r')
    dfp = open(destfile, 'w')

    slist = sfp.readlines()
    for instr in slist:
        dfp.writelines(instr)

    sfp.close()
    dfp.close()

    print('srcfile.txt 파일에서 destfile.txt 파일로 복사되었습니다.')
else:
    print('srcfile.txt 파일은 이 세상에 존재하지 않습니다.')
