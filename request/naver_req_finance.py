import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com')
soup = BeautifulSoup(response.text, 'html.parser')

trs = soup.select('#_topItems1 > tr')

names = []
prices = []
day_to_day = []
rates = []

for tr in trs:
    names.append(tr.select('th > a')[0].text)
    prices.append(tr.select('td')[0].text)
    day_to_day.append(tr.select('td')[1].text)
    rates.append(tr.select('td')[2].text.strip())  # 공백 제거 후 저장

df = pd.DataFrame()
df['종목명'] = names
df['현재가'] = prices
df['전일대비'] = day_to_day
df['등락률'] = rates

df.to_csv('../files/naver_req_finance.csv', encoding='utf-8-sig', index=False)
df.to_excel('../files/naver_req_finance.xlsx', index=False)
