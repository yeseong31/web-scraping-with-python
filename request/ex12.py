import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.naver.com')

response.raise_for_status()    # 해당 URL에 대한 접근이 문제가 있다면 에러 출력
print(f'응답 코드: {response.status_code}')

soup = BeautifulSoup(response.text, 'html.parser')

# 태그의 속성을 지정하여 데이터 추출
img_tag = soup.select('.news_logo')
for i in img_tag:
    print(i.get('alt'))

a_tag = soup.select('#NM_ONELINE_ROLLING > div > a')
for a in a_tag:
    print(a.text)
