# naver_fin_top.py

import pandas as pd
from bs4 import BeautifulSoup

f = open('../html/naver_fin_top.html', 'r', encoding='utf-8-sig')
data = f.read()
f.close()

soup = BeautifulSoup(data, 'html.parser')


def space_clear(clear_data):
    clear_data = clear_data.replace(' ', '')
    return clear_data


def escape_clear(clear_data):
    clear_data = clear_data.replace('\n', ' ')
    return clear_data


name = soup.select('#_topItems1 > tr > th > a')
# print(name)
names = []
for n in name:
    tmp = space_clear(n.text)
    tmp = escape_clear(tmp)
    names.append(tmp)

trs = soup.select('#_topItems1 > tr')

prices = []  # 현재가
day_to_day = []  # 전일대비
rates = []  # 등락률

for tr in trs:
    prices.append(tr.select('td')[0].text)
    day_to_day.append(tr.select('td')[1].text)
    rates.append(tr.select('td')[2].text)

df = pd.DataFrame()
df['종목명'] = names
df['현재가'] = prices
df['전일대비'] = day_to_day
df['등락률'] = rates

df.to_excel('../files/naver_fin_top.xlsx', index=False)
df.to_csv('../files/naver_fin_top.csv', encoding='utf-8-sig', index=False)
