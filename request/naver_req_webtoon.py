# naver_req_webtoon.py

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

ranks = list(range(1, 11))

name = soup.select('#realTimeRankFavorite > li > a')
names = [n.text for n in name]


def clear(clear_data):
    for escape in "\n\t":
        clear_data = clear_data.replace(escape, "")
    return clear_data


rate = soup.select('#realTimeRankFavorite > li > span')
rates = []
for r in rate:
    tmp = clear(r.text)
    if tmp != ' 0':
        tmp = " " + tmp
    rates.append(r.select_one('img').get('alt') + tmp)

df = pd.DataFrame()
df['순위'] = ranks
df['웹툰명'] = names
df['변동률'] = rates

df.to_excel('../files/naver_req_webtoon.xlsx', index=False)
