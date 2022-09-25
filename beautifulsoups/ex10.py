from bs4 import BeautifulSoup
from ex_html import get_html

data = get_html()
soup = BeautifulSoup(data, 'html.parser')

# 아이디 선택자
print(soup.select_one('#care1'))
print(soup.select_one('#care2'))
print(soup.select_one('#care3')) # 하위 태그 가져옴
print(soup.select_one('#care4'))
print()

# 클래스 선택자
print(soup.select_one('.lab1'))
print(soup.select_one('.lab2'))
print(soup.select_one('.lab3')) # 하위 태그 가져옴
print(soup.select_one('.lab4'))
print()

# 속성 선택자
print(soup.select_one('div[id="care1"]'))
print(soup.select_one('div[class="lab1"]'))
print(soup.select_one('a[href]'))






