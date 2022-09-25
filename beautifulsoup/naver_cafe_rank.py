import pandas as pd
from bs4 import BeautifulSoup

f = open('../html/naver_cafe_rank.html', 'r', encoding='utf-8-sig')
data = f.read()
f.close()

soup = BeautifulSoup(data, 'html.parser')

# 순위(숫자)
rank = soup.select('strong[class="txt"]')
ranks = [x.text for x in rank]
print(ranks)

# 팬카페 이름
name = soup.select('.name_area')
names = [x.text.strip() for x in name]
print(names)

# 팬카페 멤버 수
member_count = soup.select('em[aria-label="멤버수"]')
member_counts = [x.text for x in member_count]
print(member_counts)

# 팬카페 점수
score = soup.select('.cell_level > em')
scores = [x.text for _, x in score]
print(scores)

# 파일 저장
df = pd.DataFrame()
df['순위'] = ranks
df['카페명'] = names
df['멤버수'] = member_counts
df['점수'] = scores

df.to_excel('../files/naver_cafe_rank.xlsx', index=False)
