import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome 브라우저 열기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(1)

# 사이트 요청
driver.get('https://www.naver.com')
time.sleep(1)

# 뒤로 가기
driver.back()
time.sleep(1)

# 앞으로 가기
driver.forward()
time.sleep(1)

# 브라우저 닫기
driver.close()
