# naver_webtoon_rank.py

import pandas as pd
from bs4 import BeautifulSoup

f = open('../html/naver_webtoon_rank.html', 'r', encoding='utf-8-sig')
data = f.read()
f.close()

soup = BeautifulSoup(data, 'html.parser')

ranks = list(range(1, 11))

names = []
name = soup.select('#realTimeRankFavorite > li > a')
for n in name:
    names.append(n.text)

rate = soup.select('#realTimeRankFavorite > li > span')
rates = []


def clear(clear_data):
    for escape in "\n\t":
        clear_data = clear_data.replace(escape, "")
    return clear_data


for r in rate:
    tmp = clear(r.text)
    if tmp != ' 0':
        tmp = " " + tmp
    rates.append(r.select_one('img').get('alt') + tmp)

df = pd.DataFrame()
df['순위'] = ranks
df['웹툰명'] = names
df['변동률'] = rates

df.to_excel('../files/naver_webtoon_rank.xlsx', index=False)
