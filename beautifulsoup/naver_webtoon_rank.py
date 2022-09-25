# naver_webtoon_rank.py

import pandas as pd
from bs4 import BeautifulSoup

# 네이버 웹툰 순위
f = open('naver_webtoon_rank.html', 'r', encoding='utf-8-sig')
data = f.read()
f.close()

soup = BeautifulSoup(data, 'html.parser')

# 순위(숫자)
ranks = list(range(1, 11))

# 웹툰 제목
title = soup.select('#realTimeRankFavorite > li > a')
titles, sub_titles = [], []
for x in title:
    a, *b = x.text.strip().split('-')
    titles.append(a)
    sub_titles.append(''.join(b))

# 상승/하락 문자열 및 숫자
changes = soup.select('.rankBox')
change_strs, change_nums = [], []
for x in changes:
    s, n = x.img['title'], x.text.strip()  # x.img['title'] == x.img.get('title')
    change_strs.append(x.img['title'])
    change_nums.append(x.text.strip())

# 파일 저장
df = pd.DataFrame()
df['순위'] = ranks
df['제목'] = titles
df['회차'] = sub_titles
df['순위변동'] = change_strs
df['순위변동폭'] = change_nums

df.to_excel('../file/naver_webtoon_rank.xlsx', index=False)
