from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com')

# XPATH로 요소 탐색
element = driver.find_element(By.XPATH, '//*[@id="NM_ONELINE_ROLLING"]')
element.click()

driver.close()
