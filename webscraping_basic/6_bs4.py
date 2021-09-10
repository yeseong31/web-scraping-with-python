import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# res.text를 lxml로 parse하여 BeautifulSoup 객체로 만듦
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)     # HTML element에 바로 접근 가능
# print(soup.title.get_text())

# print(soup.a)         # soup 객체에서 처음 발견되는 <a> 태그 정보를 출력
# print(soup.a.attrs)   # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))     # class="Nbtn_upload"인 a element를 찾음
# print(soup.find(attrs={"class": "Nbtn_upload"}))          # class="Nbtn_upload"인 어떤 element를 찾음

# print(soup.find("li", attrs={"class": "rank01"}))
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기-시즌2 2화 PT (1)")
print(webtoon)
