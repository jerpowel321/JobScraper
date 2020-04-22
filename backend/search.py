import requests
from bs4 import BeautifulSoup


print("This is the search page")

class Job():
    def __init__(self,post):
        self.title = post.title
        self.company_name = post.name
        self.location = post.location
        self.url = post.url

def monster(q, location):
    baseURL="https://www.monster.com/jobs/search/?"
    q="q=Web-Developer"
    location="&where=San-Francsico"
    url=baseURL+q+location
    print(url)


    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    # print(results.prettify())

    job_elems = results.find_all('section', class_='card-content')
    python_jobs = results.find_all('h2', string=lambda text: 'developer' in text.lower())
    # for job_elem in job_elems:
    #     title_elem = job_elem.find('h2', class_='title')
    #     company_elem = job_elem.find('div', class_='company')
    #     location_elem = job_elem.find('div', class_='location')
    #     if None in (title_elem, company_elem, location_elem):
    #         continue
    #     print(title_elem.text.strip())
    #     print(company_elem.text.strip())
    #     print(location_elem.text.strip())
    #     print()

    for p_job in python_jobs:
        link = p_job.find('a')['href']
        print(p_job.text.strip())
        print(f"Apply here: {link}\n")

    print(len(python_jobs))