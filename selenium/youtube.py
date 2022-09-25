import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.youtube.com/'
driver.get(url)
time.sleep(2)

for i in range(0, 5000, 100):
    driver.execute_script(f'window.scrollTo(0, {i})')

response = driver.page_source
soup = BeautifulSoup(response, 'html.parser')
driver.close()

title = soup.select('#video-title')
for t in title:
    print(t.text)
