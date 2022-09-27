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

hour = int(input('시를 입력하세요 '))
minute = int(input('분을 입력하세요 '))
print('현재 시간은 {0}시 {1}분 입니다' .format(hour, minute))


'''

'''

# 문자/문자열 개수 알아내기

string1 = '간장공장공장장은 강 공장장이고 된장 공장 공장장은 공 공장장이다'
string2 = '내가 그린 기린 그림은 잘 그린 기린 그림이고 네가 그린 기린 그림은 잘 못 그린 그림이다'

str1 = string2.count('그린')
str2 = string2.count('기린')
str3 = string2.count('그림')

print("그린의 개수 : %d" % str1)
print("기린의 개수 : %d" % str2)
print("그림의 개수 : %d" % str3)

'''

'''
# 문자열의 위치 찾기 : 내가 찾고 싶은 문자가 처음 나온 위치
# 위치 = 문자열.find('검색할 문자')
# 위치 = 문자열.index('검색할 문자')

string1 = '간장공장공장장은 강 공장장이고 된장 공장 공장장은 공 공장장이다'
string2 = '내가 그린 기린 그림은 잘 그린 기린 그림이고 네가 그린 기린 그림은 잘 못 그린 그림이다'

str1 = string1.find('공')
str2 = string1.index('장')


print("공의 위치 : %d" % str1)
print("장의 위치 : %d" % str2)

'''

'''

# 문자열 삽입 및 분리
# 새로운 문자열 = 구분자 join(문자열)

train_str = '칙칙폭폭'
num_str = '123456789'

div_str1 = '-'.join(train_str)
div_str2 = '-'.join(num_str)

print(div_str1)
print(div_str2)

ani_list = ['강아지', ' 고양이', '원숭이', '코끼리']
time_list = ['12', '30', '55']

ani_list = '+'.join(ani_list)
time_list = ':'.join(time_list)

print(ani_list)
print(time_list)

'''

'''
# 기존 문자열을 특정 구분자로 구분하는 기능

planet_str = '수성-금성-지구-화성-목성'
time_str = '12시:30분:55초'

planet_list = planet_str.split('-')
time_list = time_str.split(':')

print(planet_list)
print(time_list)

'''

'''

# 대소문자 변환하기

eng_str = input("영문자를 입력하세요 ")

upper_str = eng_str.upper()
lower_str = eng_str.lower()

print('대문자로 변환 : %s' % upper_str)
print('소문자로 변환 : %s' % lower_str)

'''

'''
# 문자열 공백 없애기
string1 = ' 죽는 날까지 하늘을 우러러'
string2 = '한점 부끄러움이 없기를 '
string3 = ' 잎새에 이는 바람에도 '

lstrip_str = string1.lstrip()
rstrip_str = string2.lstrip()
strip_str = string3.lstrip()

print('string1 : %s ' % string1)
print('string1 : %s ' % string2)
print('string1 : %s ' % string3)
print()
print("왼쪽 공백없애기 :%s" % lstrip_str)
print("오른쪽 공백없애기 :%s" % rstrip_str)
print("양쪽 공백없애기 :%s" % strip_str)
'''
# 문자열 구성 파악하기


while True:
    string = input('문자열을 입력하세요 : ')

    if string.isdigit():
        print('문자열은 숫자로 구성되어 있습니다')
    elif string.isalpha():
        print('문자열은 글자로 구성되어 있습니다')
        if string.isupper():
            print("문자열은 대문자로 구성되어 있습니다")
        elif string.islower():
            print("문자열은 소문자로 구성되어 있습니다")
    elif string.isspace():
        print('문자열은 공백으로 구성되어 있습니다')
        break
    else:
        print("모르겠습니다")
    print()
