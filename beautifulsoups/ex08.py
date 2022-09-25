from bs4 import BeautifulSoup
from ex_html import get_html

data = get_html()
print(type(data))

# BeautifulSoup(변환(분석)할 데이터, '분석(변환) 도구 이름')
soup = BeautifulSoup(data, 'html.parser')
print(type(soup))

print(soup.body)
print()
print(soup.div)
print()
print(soup.span)
print()
print(soup.a)
