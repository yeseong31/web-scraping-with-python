from selenium.webdriver.common.by import By

# selenium에서 요소의 위치를 찾을 때 사용하는 속성들

# html tag id 속성
print(By.ID)
# html tag
print(By.TAG_NAME)
# html tag name 속성
print(By.CLASS_NAME)
# css selector 방식
print(By.CSS_SELECTOR)
# 링크와 텍스트
print(By.LINK_TEXT)
# 링크 텍스트의 자식 텍스트
print(By.PARTIAL_LINK_TEXT)
# 태그의 경로, XPATH(XML Path): 문서를 탐색하고 선택하는 데 사용
print(By.XPATH)
