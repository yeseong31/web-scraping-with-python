import pandas as pd

names = ['김변수', '이상수', '박참조']
points = [100, 200, 300]
positions = ['공격수', '수비수', '미드필더']

# 데이터를 DataFrame으로 저장
df = pd.DataFrame()
df['이름'] = names
df['포인트'] = points
df['포지션'] = positions

df.to_csv('../file/file03.csv', encoding='utf-8-sig', index=False)
df.to_excel('../file/file04.xlsx', index=False)
