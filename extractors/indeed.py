import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    base_url = 'https://kr.indeed.com'
    sub_url = '/m/jobs?from=mobRdr&q='

    driver.get(f'{base_url}{sub_url}{keyword}')
    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')

    # pagination
    pagination = soup.select('.jobsearch-LeftPane > nav > div')
    if pagination is None:
        return 1
    count = len(pagination)
    driver.close()

    if count >= 5:
        return 5
    return count


def extract_indeed_jobs(keyword):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    base_url = 'https://kr.indeed.com'
    pages = get_page_count(keyword)

    print(f'Found: {pages} pages')

    # 페이지 수만큼 스크래핑
    results = []
    for page in range(pages):
        final_url = f'{base_url}/m/jobs?q={keyword}&start={page*10}'
        print(f'Requesting... {final_url}')
        driver.get(final_url)
        response = driver.page_source

        soup = BeautifulSoup(response, 'html.parser')
        job_list = soup.find('ul', class_='jobsearch-ResultsList')
        jobs = job_list.find_all('li', recursive=False)  # recursive=False: 바로 하위의 li만을 타겟으로 함

        for job in jobs:
            # 필요 없는 li 제거
            zone = job.find('div', class_='mosaic-zone')
            if zone is None:
                anchor = job.select_one('h2 a')
                title = anchor['aria-label']
                link = anchor['href']
                company_name = job.find('span', class_='companyName')
                company_location = job.find('div', class_='companyLocation')

                job_data = {
                    'link': f'{base_url}{link}',
                    'company': company_name.text.replace(',', ''),
                    'location': company_location.text.replace(',', ''),
                    'position': title.replace(',', '')
                }
                results.append(job_data)

    driver.close()
    return results
