import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.instagram.com'
driver.get(url)

# 로그인
user_id = os.environ.get('INSTAGRAM_USERNAME')
user_pw = os.environ.get('INSTAGRAM_PASSWORD')
search_data = '종로맛집'
time.sleep(5)

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys(user_id)
password.send_keys(user_pw)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(5)

# 나중에 하기 버튼클릭
driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button').click()
time.sleep(5)

# 나중에 하기 버튼 클릭
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/'
                    'div/div/div[3]/button[2]').click()
time.sleep(5)

# 해시태그 검색
element = driver.find_element(By.XPATH,
                              '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/'
                              'div/div/div[2]/input')
element.send_keys(search_data)
time.sleep(5)

# 검색 결과 중 첫번째 선택
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/'
                    'div[3]/div/div[2]/div/div[1]/div/a/div/div[2]/div[1]/div/div').click()


# 스크롤 내리기
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # Javascript 코드 실행
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()

# print(soup)
