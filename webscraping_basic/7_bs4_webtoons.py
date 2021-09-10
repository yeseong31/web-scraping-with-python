import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# res.text를 lxml로 parse하여 BeautifulSoup 객체로 만듦
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
  print(cartoon.get_text())