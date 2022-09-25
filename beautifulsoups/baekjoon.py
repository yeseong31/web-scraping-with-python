# 백준 단계별로 풀어보기 웹페이지 스크래핑 연습
import collections

import requests
from bs4 import BeautifulSoup

url = "https://www.acmicpc.net/step"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

main_page = soup.find("table", attrs={"class": "table table-bordered table-striped"}).tbody
dic = collections.defaultdict(list)

print("*** 백준 - '단계별로 풀어보기' 문제 스크래핑 ***")
print("*** 단계   [문제 번호, 제목, 정답, 제출, 설명]  ***")

for i, step in enumerate(main_page):
    step_url = url[:-5] + step.a["href"]
    res = requests.get(step_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    problems = soup.find("table",
                         attrs={"class": "table table-striped table-bordered sortable-table clickable-table",
                                "id": "problemset"}).tbody

    lst = [[] for _ in range(len(problems) // 2)]
    idx = 0
    for problem in problems:
        check = problem.td
        # 설명란이 아니라면
        if len(problem) == 1:
            lst[idx].append(check.get_text())
            dic[str(f'{i + 1}-{idx + 1}')] = lst[idx]
            idx += 1
        else:
            # 문제 번호
            n = check.next_sibling
            lst[idx].append(int(n.get_text()))
            # 제목
            title = n.next_sibling
            lst[idx].append(title.get_text())
            # 정답자 수
            correct = title.next_sibling.next_sibling
            lst[idx].append(int(correct.get_text()))
            # 제출자 수
            submission = correct.next_sibling
            lst[idx].append(int(submission.get_text()))
            # 정답 비율
            # ratio = round(int(correct.get_text()) * 100 / int(submission.get_text()), 3)
            # lst[idx].append(ratio)

# for d in dic:
#     print(d, '\t', dic[d])

with open("../files/baekjoon.txt", "w", encoding="utf8") as f:
    for d in dic:
        f.write(f'{d} \t{dic[d]}\n')
