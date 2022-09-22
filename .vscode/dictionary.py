'''
product = {'컵라면': 700, '삼각김밥': 1000, '소세지': 1500}

word = {'boy': "소년", 'girl': '소녀'}
word['son'] = '아들'

product['아이스크림'] = 1000
product['밀크티'] = 2000
word['house'] = '집'

print(product.get("아이스크림"))
print(list(product.keys()))  # 리스트 형태로 출력되어 딕셔너리의 형태로 감싸져 있음.
print(list(product.values()))  # 수정본

# 해당 딕셔너리에서 해당 키가 있는지 확인하는 방법(in)
# 키 in 딕셔너리 이름

item = input('상품의 이름을 입력하세요 : ')

if (item in product):
    print('상품이 있습니다.')
else:
    print("상품이 없습니다.")
'''
# 나라 이름 입력하면 나라의 수도 이름이 출력되는 프로그램

capital = {'네팔': '카트만두', '대한민국': '서울', '중국': '베이징',
           '일본': '도쿄', "이탈리아": "로마", "러시아": "모스크바", '독일': '베를린', '미국': "워싱턴", '프랑스': '파리', '영국': '런던'}

while (True):
    country = input(str(list(capital.keys())) + '나라의 수도는 무엇일까요? ')

    if country in capital:
        print(country, "의 수도는 ", capital.get(country), "입니다")
    elif country == 'q':
        break
    else:
        print('그런 나라가 없습니다.')
