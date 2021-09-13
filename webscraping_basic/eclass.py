import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# e-class
browser = webdriver.Chrome('../chromedriver.exe')

# 1. 홈페이지 이동
browser.get('http://eclass.kpu.ac.kr/ilos/main/main_form.acl')

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('header_login_img')
elem.click()

# 3. 아이디와 비밀번호 정보 get
# f = open('../data/eclass.txt', 'r')
# id = f.readline()
# pw = f.readline()
# f.close()

with open('../data/eclass.txt', 'r') as f:
    id = f.readline()
    pw = f.readline()

# 4. 얻은 정보들로 로그인 진행
browser.find_element_by_id('usr_id').send_keys(id)
browser.find_element_by_id('usr_pwd').send_keys(pw)
browser.find_element_by_id('login_btn').click()

# 5. 딥러닝프레임워크 수업 제일 최근의 강의자료 다운로드
browser.find_element_by_xpath('//*[@id="contentsIndex"]/div[2]/div[2]/ol/li[3]/em').click()  # li[1]~[7]로 강의 선택
browser.find_element_by_xpath('//*[@id="submain-contents"]/div[2]/div[5]/div[2]/ol/li[1]/em/a').click()
# browser.find_element_by_xpath('//*[@id="tbody_file"]/div[2]/div/a').click()

# 6. 2주차 첫 번째 온라인 강의 듣기
browser.back()
browser.find_element_by_id('week-2').click()
browser.find_element_by_xpath('//*[@id="lecture-2"]/div/ul/li[2]/img').click()  # 'lecture-2'는 전체 영상의 순서 중 2번째

try:
    alert = browser.switch_to.alert
    alert.accept()
    # alert.dismiss()
except:
    print('There is no alert')

# elem = browser.find_element_by_id('6130d4c1452ac-page')
# browser.switch_to.frame(elem)
# browser.find_element_by_class_name('vc-front-screen-play-btn').click()
