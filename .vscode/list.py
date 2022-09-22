'''
ktx = [10, 20, 30, 40, 50, 60, 70]


print(ktx[:2])  # 리스트 타입으로 리턴.마지막 번호는 포함되지 않음. 마지막 번호 출력 X
print(ktx[:5])
print(ktx[2:6])

파이썬을 사용할 때에는 콜론(:)과 들여쓰기를 빼놓지 말자!! 특히나 함수 쓸 때!!

'''
from audioop import reverse


ktx = [10, 20, 30, 40, 50, 60, 70]

print("현재 리스트 : ", ktx)

ktx.append(50)

print("현재 리스트 : ", ktx)

ktx.pop()
print("현재 리스트 : ", ktx)

ktx.reverse()
print("현재 리스트 : ", ktx)

ktx.sort()
print("현재 리스트 : ", ktx)

ktx.remove(70)
print("현재 리스트 : ", ktx)

ktx.insert(1, "이루다")
print("현재 리스트 : ", ktx)

tgv = [100, 200, 300]

ktx.extend(tgv)

print("현재 리스트 : ", ktx)

idx = ktx.index(40)
print(idx)

lens = len(ktx)

print("길이 : ", lens)