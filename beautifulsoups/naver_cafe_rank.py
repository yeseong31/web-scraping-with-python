import pandas as pd
from bs4 import BeautifulSoup

f = open('../html/naver_cafe_rank.html', 'r', encoding='utf-8-sig')
data = f.read()
f.close()

soup = BeautifulSoup(data, 'html.parser')

# 네이버 카페 등수 
rank = soup.select('strong[class="txt"]')
ranks = []
for r in rank:
    ranks.append(r.text)

# 네이버 카페 이름
name = soup.select('strong[class="name"]')
names = []
for n in name:
    names.append(n.text)

# 네이버 카페 멤버수
member_count = soup.select('em[aria-label="멤버수"]')
member_counts = []
for mc in member_count:
    member_counts.append(mc.text)

# 네이버 카페 점수
scores = []
score = soup.select('.cell_level > em')
for s in score:
    scores.append(s.text[2:])

df = pd.DataFrame()
df['카페등수'] = ranks
df['카페명'] = names
df['멤버수'] = member_counts
df['점수'] = scores

df.to_excel('../files/naver_cafe_rank.xlsx', index=False)
df.to_csv('../files/naver_cafe_rank.csv', encoding='utf-8-sig', index=False)