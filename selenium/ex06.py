from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 네이버 사전으로 이동
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com')

# element = driver.find_element(By.LINK_TEXT, '사전')
# element.click()

elements = driver.find_elements(By.CLASS_NAME, 'nav')
for element in elements:
    a = element.get_attribute('data-clk')
    if a == 'svc.dic':
        element.click()
        break

driver.close()
