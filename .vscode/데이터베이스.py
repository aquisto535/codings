
import sqlite3

conn = sqlite3.connect('bookStoreDB')

print('1. DB 연결 성공')

cur = conn.cursor()

print('2. 커서 생성 성공')

cur.execute(
    'create table if not exists bookitem (item char(100), author char(50), publisher char(50), stock int)')
print('3. 테이블생성')


cur.execute(
    "insert into bookitem values('java', 'lch', 'ebook', 200)")
cur.execute(
    "insert into bookitem values('C++', 'kim', 'digital', 300)")
cur.execute(
    "insert into bookitem values('C#', 'park', 'habit', 400)")
cur.execute(
    "insert into bookitem values('python', 'cho', 'ebook', 500)")

# 삭제 cur.execute('delete from bookitem / delete from bookitem where 조건')

print('4. 데이터 입력')

conn.commit()  # 데이터 저장

print('5. 데이터 저장')

cur.execute('select * from bookitem')  # 전체 출력


print('6. 데이터 조회')


while True:
    row = cur.fetchone()  # 한 행씩 출력함.

    if (row == None):
        break
    print(row)

print('7. 데이터 출력')

conn.close()
print('8. DB 연결 종료')
