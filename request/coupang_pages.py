import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0"}

for i in range(1, 6):
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP" \
          f"&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter" \
          f"=&isPriceRange=false&brand=&offerCondition=&rating=0&page=" \
          f"{i}&rocketAll=false&searchIndexingToken=1=4&backgroundColor= "
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()
        # Apple 제품은 제외
        if 'Apple' in name:
            continue

        price = item.find("strong", attrs={"class": "price-value"}).get_text()

        rate = item.find("em", attrs={"class": "rating"})
        # 리뷰 1000개 이상, 평점 5.0 이상만 조회
        if not rate:
            continue
        rate = rate.get_text()

        rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
        if not rate_cnt:
            continue
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]

        link = item.find('a', attrs={'class': 'search-product-link'})['href']

        if int(rate_cnt) >= 100 and float(rate) >= 5.0:
            print(f'제품명: {name}')
            print(f'가격: {price}')
            print(f'평점(리뷰): {rate}({rate_cnt})')
            print(f'바로가기: {"https://www.coupang.com" + link}')
            print('-' * 100)
