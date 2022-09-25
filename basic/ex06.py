import pandas as pd

names = ["김변수", "이상수", "박참조"]
points = [100, 200, 300]
positions = ["공격수", "수비수", "미드필더"]

# pip install pandas
df = pd.DataFrame()
df['이름'] = names
df['포인트'] = points
df['포지션'] = positions

# 클래스 안에 함수: 메서드(method)
# df.to_csv() csv 파일로 데이터프레임 데이터 저장
# df.to_excel()  엑셀 파일로 데이터프레임 데이터 저장
df.to_csv('../files/file03.cvs', encoding='utf-8-sig', index=False)

df.to_excel('../files/file04.xlsx', index=False)
