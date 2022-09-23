# 인덱스 통해 역순 출력
'''
str1 = '다시 합창 합시다'
str2= ''


count = len(str1) #str1.length

for i in range(0, count):
    str2 += str1[count - (i + 1)]

print('str1 : ', str1)
print('str2 : ', str2)
'''

# 인덱스를 통해 문자열을 자르기(분리하기)
'''
str = 'to be or not to be'

print(str[0:5])
print(str[6:8])
print(str[9:16])

'''

# 문자열 서식 지정과 포매팅

'''
value = int(input('정수값을 대입하세요 '))
print('현재 시간은 %d시 입니다' % value)
value = float(input('실수값을 대입하세요 '))
print('현재 체온은 %.1f도 입니다' % value)

'''


hour = int(input('시를 입력하세요 '))
minute = int(input('분을 입력하세요 '))
print('현재 시간은 {0}시 {1}분 입니다' .format(hour, minute))
