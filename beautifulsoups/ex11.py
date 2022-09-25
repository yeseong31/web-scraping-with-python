from ex_html import get_html
from bs4 import BeautifulSoup

data = get_html()

soup = BeautifulSoup(data, 'html.parser')

# 결과 None , 계층 접근은 중간에 생략하지 말자.
print(soup.select_one('html > div')) 
print()
print(soup.select_one('body > div'))
print(soup.select('body > div'))
print()

# 꼭 최상위에서 접근이 아니어도 됨
print(soup.select_one('div > span')) 
print()

# 다른 선택자 가능
print(soup.select_one('body > .lab3 > #care4'))


