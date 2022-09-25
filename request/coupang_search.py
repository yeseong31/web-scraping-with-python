import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP" \
      "&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange" \
      "=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor= "
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

for item in items:
    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("---<광고 상품 제외>---")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()
    # Apple 제품은 제외
    if 'Apple' in name:
        print("---<Apple 상품 제외>---")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text()
    rate = item.find("em", attrs={"class": "rating"})

    # 리뷰 1000개 이상, 평점 5.0 이상만 조회
    if rate:
        rate = rate.get_text()
    else:
        rate = '평점 없음'
        print('---<평점 없는 상품 제외>---')
        continue
    rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        rate_cnt = '평점 수 없음'
        print('---<평점 수 없는 상품 제외>---')
        continue

    if int(rate_cnt) >= 1000 and float(rate) >= 5.0:
        print(name, price, rate, rate_cnt)
