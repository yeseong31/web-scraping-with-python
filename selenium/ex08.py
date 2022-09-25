from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 네이트 '실시간 이슈 키워드' 얻기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://news.nate.com/search?q=any'
driver.get(url)

# selenium > BeautifulSoup
response = driver.page_source
driver.close()  # 더 이상 selenium이 필요하지 않으므로 미리 종료

soup = BeautifulSoup(response, 'html.parser')
kwd_list_a = soup.select('.kwd-list > a')

for a in kwd_list_a:
    print(a.text)
