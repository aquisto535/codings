'''
from bs4 import BeautifulSoup

homepage = open('ediya.html', 'r', encoding='utf-8')
html_doc = homepage.read()

homepage.close()

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.find_all('p', class_='each-menu')

for data in result:
    print(data.text)

'''

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'mozilla/5.0'}

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, 'html.parser')

'''
ul 속 데이터 출력
for child in soup.ul.children:
    print(child.string)

'''

# print(soup.find_all('h2'))

# ol, ul 포함된 리소스를 모두 긁어오고 싶다면?

'''
for data in soup.find_all('h2'):
print(data)

'''

# print(soup.find_all(re.compile('[ou]l'))) #ol , ul 정규식으로 동시 찾기

# print(soup.find_all(re.compile('h[1-3]'))) h1~h3 정규식으로 동시 찾기

#print(soup.find_all(['h1', 'p']))


title = soup.select('.card-title')  # 선택자 지정하여 사용

for t in title:
    print(t.get_text())

'''
download = soup.select('#hot-articles-go-download')
print(download)

'''
