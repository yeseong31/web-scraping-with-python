import requests

# res = requests.get('http://nadocoding.tistory.com')
# res = requests.get('http://naver.com')

res = requests.get('http://eclass.kpu.ac.kr/ilos/main/main_form.acl')
res.raise_for_status()    # 해당 URL에 대한 접근이 문제가 있다면 에러 출력

# print("응답코드: ", res.status_code)    # 200: 정상 / 403: 권한 없음

# if res.status_code == requests.codes.ok:
#   print("정상입니다.")
# else:
#   print("문제가 생겼습니다. [에러 모드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("eclass.html", "w", encoding="utf8") as f:
  f.write(res.text)

