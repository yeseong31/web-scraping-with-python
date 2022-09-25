# naver_fin_top.py

import pandas as pd
from bs4 import BeautifulSoup

f = open('../html/naver_fin_top.html', 'r', encoding='utf-8-sig')
data = f.read()
f.close()

soup = BeautifulSoup(data, 'html.parser')

# 종목명
event_name = soup.select('tbody > tr > th > a')
event_names = [' '.join(x.text.replace('\n', ' ').strip().split()) for x in event_name]

# 현재가
target = soup.select('tbody > tr > td')

price, prev, rate = [], [], []
for i in range(0, len(target), 3):
    a, b, c = target[i:i + 3]
    # 현재가
    price.append(a.text)
    # 전일대비
    prev.append(b.text)
    # 등락률
    rate.append(c.text)

# 파일 저장
df = pd.DataFrame()
df['종목명'] = event_names
df['현재가'] = price
df['전일대비'] = prev
df['등락률'] = rate

df.to_excel('../files/naver_fil_top.xlsx', index=False)
df.to_csv('../files/naver_fin_top.csv', encoding='utf-8-sig', index=False)
