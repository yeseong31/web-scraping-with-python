import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com')

# 네이버 검색어 입력
element = driver.find_element(By.ID, 'query')

search_word = '아이패드'
element.send_keys(search_word)
element.send_keys(Keys.ENTER)  # '엔터' 입력

# 응답 결과를 BeautifulSoup로 처리할 수도 있음
# response = driver.page_source
# soup = BeautifulSoup(response, 'html.parser')
# print(soup)

time.sleep(3)

driver.close()
