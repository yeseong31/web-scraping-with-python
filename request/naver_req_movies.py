# naver_req_movie.py

# 특정 '기간' 동안의 네이버 영화 정보 추출 (평점순)
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 날짜 포맷 변경
# https://www.geeksforgeeks.org/python-strftime-function/

dates = pd.date_range('20220901', periods=24)

rows = []

for date in dates:
    date = date.strftime("%Y%m%d")  # 날짜 포맷 변경
    url = f'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={date}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 영화 제목(1 ~ 10위)
    title = soup.select('.tit5 > a')
    titles = [t.text for t in title[:10]]

    # 평점(1 ~ 10위)
    point = soup.select('.point')
    points = [p.text for p in point[:10]]

    # 전체 수집 내용 저장
    for i in range(len(titles)):
        rows.append([date, titles[i], float(points[i])])

df = pd.DataFrame(rows, columns=['날짜', '영화 제목', '평점'])

# 피벗 테이블 생성
pivot_data = pd.pivot_table(df, index='영화 제목', aggfunc=np.mean)
pivot_data = pivot_data.sort_values(by='평점', ascending=False)
print(pivot_data)

# df.to_excel('../files/naver_req_movies.xlsx', index=False)
