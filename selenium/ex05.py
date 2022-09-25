from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com')

# element = driver.find_element(By.CLASS_NAME, 'news_logo')
# print(f'element: {element}')
# print(f'element.tag_name: {element.tag_name}')
# print(f'element.get_property: {element.get_property("alt")}')

elements = driver.find_elements(By.CLASS_NAME, 'news_logo')  # BeautifulSoup select()와 동일
for element in elements:
    print(f'element.get_property: {element.get_property("alt")}')

driver.close()
