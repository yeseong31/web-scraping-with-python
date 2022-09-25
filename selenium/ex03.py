from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com')

# 화면 내 요소를 id, class 등의 selector를 이용하여 찾을 수 있음
element = driver.find_element(By.ID, 'NM_ONELINE_ROLLING')
print(f'element: {element}')
print(f'element.tag_name: {element.tag_name}')
print(f'element.text: {element.text}')

element.click()

driver.close()
