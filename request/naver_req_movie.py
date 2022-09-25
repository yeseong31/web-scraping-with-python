# naver_req_movie.py

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220923'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.select('.tit5 > a')
titles = [t.text for t in title[:10]]

point = soup.select('.point')
points = [p.text for p in point[:10]]

df = pd.DataFrame()
df['제목'] = titles
df['평점'] = points

df.to_excel('../files/naver_req_movie.xlsx', index=False)
