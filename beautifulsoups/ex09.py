from bs4 import BeautifulSoup
from ex_html import get_html

data = get_html()

# BeautifulSoup(변환(분석)할 데이터, '분석(변환) 도구 이름')
soup = BeautifulSoup(data, 'html.parser')

# select_one() : 매칭되는 대상 한 개만 갖고 오기 
# select() : 매칭되는 대상 모두 갖고 오기

select_one_data = soup.select_one('div')
print(select_one_data)
print()

select_data = soup.select('div')
print(select_data)

# text : 태그 안에 데이터 
print(select_one_data.text)
print()
print(select_data[0].text)
print(select_data[1].text)
print(select_data[2].text)

# get('속성명') : 속성 데이터를 추출
a_tag = soup.select_one('a')
a_tag_text = a_tag.text
a_tag_get = a_tag.get('href')
print(f'a tag 사이에 있는 데이터 : {a_tag_text}')
print(f'a tag 속성에 있는 데이터 : {a_tag_get}')
