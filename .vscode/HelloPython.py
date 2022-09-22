'''
def coffeeMachine(coffee):

    print()

    print('1. 물을 준비한다.')
    print('2. 컵을 준비한다.')

    # 커피 선택

    if coffee == '아메리카노':
        print(coffee, "아메리카노를 탄다")
    elif coffee == '카페라떼':
        print(coffee, "카페라떼를 탄다")
    elif coffee == '카페모카':
        print(coffee, "카페모카를 탄다")
    else:
        print("이름을 정확히 넣어주세요")

    print('3. 물을 붓는다.')
    print()
    print(coffee, '한잔 서비스 완료')


for i in range(0, 3):  # 자동으로 1씩 증가=(0, 3,)
    coffee = ''

    coffee = input('커피를 선택하시오(아메리카노, 카페라떼, 카페모카) : ')
    print()
    coffeeMachine(coffee)
    print()
    '''
