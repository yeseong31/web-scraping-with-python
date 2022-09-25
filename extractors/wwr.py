
from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    """We Work Repotely 페이지에서 keyword에 대한 검색 결과로
    회사명, 지역, 포지션을 반환하는 함수"""
    base_url = 'https://weworkremotely.com/remote-jobs/search?term='
    response = get(f'{base_url}{keyword}')

    result = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', class_='jobs')  # class는 예약어이므로 변수명 사용을 위해 뒤에 '_'를 붙임

        for job_section in jobs:
            for post in job_section.find_all('li')[:-1]:
                anchors = post.find_all('a')[1]
                company, kind, region = anchors.find_all('span', class_='company')
                title = anchors.find('span', class_='title')

                result.append({
                    'company': company.text,
                    'region': region.text,
                    'position': title.text,
                })

    return result
