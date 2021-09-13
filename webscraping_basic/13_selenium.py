import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 절대 경로, 상대 경로 모두 가능
browser = webdriver.Chrome('../chromedriver.exe')

# 1. 네이버 이동
browser.get('https://naver.com')

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. 아이디와 패스워드 입력
browser.find_element_by_id('id').send_keys('naver_id')      # 실제 아이디!
browser.find_element_by_id('pw').send_keys('naver_pw')      # 실제 패스워드!

# 4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

time.sleep(1)

# 5. 아이디를 새로 입력
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('new_naver_id')

# 6. html 정보 출력
print(browser.page_source)

# 7. browser 종료
# browser.close()
browser.quit()
