import os

import pandas as pd
import requests
import xmltodict
from dotenv import load_dotenv

load_dotenv()

# 인증키 입력
encoding = os.environ.get('ENCODING_KEY')
decoding = os.environ.get('DECODING_KEY')

# 기상청 단기예보 
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
params = {'serviceKey': decoding,
          'pageNo': '1',
          'numOfRows': '1000',
          'dataType': 'XML',
          'base_date': '20220924',
          'base_time': '0500',
          'nx': '55',
          'ny': '127'}

response = requests.get(url, params=params)

response = xmltodict.parse(response.content)
items = response.get('response').get('body').get('items').get('item')

# {'baseDate': '20220920', 'baseTime': '0500', 'category': 'TMP', 'fcstDate': '20220920', 'fcstTime': '0600',
# 'fcstValue': '15', 'nx': '55', 'ny': '127'

# 한 시간의 데이터는 12개의 카테고리를 갖고 있음.
rows = []
for item in items:
    if item.get('category') == "TMP":
        rows.append([item.get('fcstDate'), item.get('fcstTime'), item.get('fcstValue')])

df = pd.DataFrame(rows, columns=['날짜', '시간', '온도'])
df.to_excel('../files/weather.xlsx', index=False)
# open('weather.json', 'w', encoding='UTF-8-SIG').write(str(response))
