# 가비아 사이트를 통한 실습
import requests
import pandas as pd  # pd가 pandas를 대신함.
from bs4 import BeautifulSoup as bs

page = requests.get('https://library.gabia.com/')

soup = bs(page.text, "html.parser")

elements = soup.select('div.esg-entry-content a.eg-grant-element-0')

titles = []

links = []

for index, element in enumerate(elements, 1):
    titles.append(element.text)
    links.append(element.attrs['href'])

df = pd.DataFrame()

df['titles'] = titles  # key값 설정

df['links'] = links  # value값 설정

df.to_excel('./data.xlsx', sheet_name='sheet1')

#print("{}번째 게시글 제목 ㅣ {}, {} " .format(index, element.text, element.attrs['href']))
