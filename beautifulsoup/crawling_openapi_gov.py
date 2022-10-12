# https://www.weather.go.kr/w/index.do

import requests
from bs4 import BeautifulSoup

open_api = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'

res = requests.get(open_api)
soup = BeautifulSoup(res.content, 'xml')
locations = soup.find_all('location')

for location in locations:
    print(location.find('city').text)
    datas = soup.find_all('data')
    for data in datas:
        print(data.find('tmEf').text)
        print(data.find('wf').text)
