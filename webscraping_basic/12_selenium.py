# pip install selenium

# 실습을 위해서는 Chrome 브라우저로부터 chromedriver 설치 필요
# 내 chrome ver: 93.0.4577.63

# 터미널 실습으로 하면 진행 상황을 실시간으로 확인하면서 코딩 가능

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('../chromedriver.exe')
browser.get('https://naver.com')

# 네이버 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()
# 이전 페이지로 이동
browser.back()
browser.forward()
# 새로고침
browser.refresh()
browser.back()

# 네이버 검색
elem = browser.find_element_by_id('query')
elem.click()
# '테스트' 검색어 입력 후 enter 입력
elem.send_keys('테스트')
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name('a')
for e in browser.find_elements_by_tag_name('a'):
    e.get_attribute('href')

# xpath로 열기
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')

# 현재 탭만 닫음
browser.close()
# 모든 브라우저를 닫음
browser.quit()

# -----------------------------------------------------------------------------------------
# 네이버 로그인 자동입력 방지 우회 방법은...
# https://jaeseokim.dev/Python/python-Selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-Naver-login-%ED%9B%84-%EA%B5%AC%EB%8F%85-Feed-%ED%81%AC%EB%A1%A4%EB%A7%81/
