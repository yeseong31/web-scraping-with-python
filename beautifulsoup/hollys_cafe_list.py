from urllib import request

import pandas as pd
from bs4 import BeautifulSoup

result = []

for page_number in range(1, 54):
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_number}&sido=&gugun=&store='
    html = request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    for row in soup.select('.tb_store > tbody > tr'):
        store_td = row.find_all('td')
        place = store_td[0].text
        name = store_td[1].text
        address = store_td[3].text
        tel = store_td[5].text
        result.append((place, name, address, tel))

df = pd.DataFrame(result, columns=['지역', '매장명', '주소', '전화번호'])
df.to_excel('../files/hollys_cafe_search.xlsx', index=False)
