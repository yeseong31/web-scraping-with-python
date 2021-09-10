import requests
from bs4 import BeautifulSoup

# 백준 '단계별로 풀어보기' 페이지를 탐색해 보자
url = "https://www.acmicpc.net/step"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title.get_text())      # 홈페이지 Title 출력

# '단계별로 풀어보기' 알고리즘 50개 출력
algorithm = soup.find("table", attrs={"class": "table table-bordered table-striped"}).tbody
title, description = [], []
for algo in algorithm:
    s = algo.td.next_sibling
    title.append(s.get_text())
    description.append(s.next_sibling.get_text())

for i in range(len(title)):
    print(f'{i + 1}단계: {title[i]} - {description[i]}')

