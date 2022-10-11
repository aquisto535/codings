

'''
srcFile = 'sea.png'
destFile = input('대상 파일 명을 입력하세요')
print()

if os.path.exists(srcFile):
    sfp = open(srcFile, 'rb')
    dfp = open(destFile, "wb")

    while True:
        sbyte = sfp.read()
        if not sbyte:
            break
        dfp.write(sbyte)

    sfp.close()
    dfp.close()

    print("복사가 완료하였습니다")
else:
    print("원본파일이 존재하지 않습니다.")
'''

"""
srcFile = 'SleepAway.mp3'

print()

if os.path.exists(srcFile):
    sfp = open(srcFile, 'rb')

    while True:
        sbyte = sfp.read()
        if not sbyte:
            break

    sfp.close()

    print(" 복사가 완료하였습니다")
else:
    print(" 원본파일이 존재하지 않습니다.")
    
"""
