import requests
from bs4 import BeautifulSoup
import sqlite3
import os

fdic = {}
list_a = []
list_b = []


headers = {'User-Agent': 'mozilla/5.0'}

webpage = requests.get(
    "https://www.daangn.com/region/%EA%B2%BD%EA%B8%B0%EB%8F%84/%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%9E%A5%EC%95%88%EA%B5%AC")
soup = BeautifulSoup(webpage.content, 'html.parser')


title = soup.select('.card-title')  # 선택자 지정하여 사용
price = soup.select('.card-price')

for t in title:
    list_title = t.get_text().strip()
    list_a.append(list_title)


for p in price:
    list_price = p.get_text().strip()
    list_b.append(list_price)


for i in range(len(list_a)):
    fdic[i] = [list_a[i], list_b[i]]


conn = sqlite3.connect(os.path.dirname(__file__) + "\\fdic.db")
cur = conn.cursor()
conn.execute(
    "create table if not exists fss_dic(id integer, name text, content text)")

for i in fdic:
    name = fdic[i][0]
    content = fdic[i][1]

    sql = "insert into fss_dic values (?, ?, ?)"
    cur.execute(sql, (i, name, content))

cur.execute("select * from fss_dic")

while (True):
    row = cur.fetchone()
    if (row == None):
        break
    print(row)


conn.commit()
conn.close()
