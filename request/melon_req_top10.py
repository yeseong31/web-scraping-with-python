# melon_req_top10.py

import pandas as pd
import requests
from bs4 import BeautifulSoup

'''
-- 크롤링 필터링 --
사용자의 요청 헤더(request header)에 존재하는 속성과 값을 갖고 필터링을 함.
주로 User-Agent: Mozilla/5.0 을 확인함.(웹 브라우저의 요청인지 판단함)
필터링을 우회하기 위해서는 파이썬에서의 요청 헤더에 속성과 값을 추가해서 
요청하면 응답 데이터를 얻을 수 있음.
'''

url = 'https://www.melon.com/index.htm'
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()

# 멜론 차트 탑 10의 순위, 제목, 가수
soup = BeautifulSoup(response.text, 'html.parser')
lis = soup.select('.nth1 > .list_wrap > ul > .rank_item')

ranks = []
songs = []
artists = []
for li in lis:
    ranks.append(li.select_one('.rank_number > .rank').text + li.select_one('.rank_number > .none').text)
    songs.append(li.select_one('.ellipsis').text)
    artists.append(li.select_one('.fc_mgray').text)

df = pd.DataFrame()
df['순위'] = ranks
df['노래'] = songs
df['가수'] = artists

df.to_excel('../files/melon_req_top10.xlsx', index=False)
