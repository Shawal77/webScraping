from turtle import ht
from bs4 import BeautifulSoup
import requests
import time

#search_word = 'python'
given_url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
unfirmiliar_skill = 'Python2'
TIME_WAIT = 10

def find_jobs():
    html_data = requests.get(url=given_url).text
    soup = BeautifulSoup(html_data, 'lxml')

    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span',class_='srp-skills').text.replace(' ','')
        date_pubilsh = job.find('span',class_='sim-posted').span.text
        link_more_info = job.h2.a['href']
        #print(date_pubilsh)
        if unfirmiliar_skill not in skills:
            result = (f'''
    Company Name: {company_name.strip()}
    Skills: {skills.strip()}
    Link: {link_more_info}''')
            with open(f'posts/{index}.txt','w') as f:
                f.writelines(result)
            print('file saved')

if __name__ == '__main__':
    while True:
        find_jobs()
        print(f'waiting {TIME_WAIT} seconds')
        time.sleep(TIME_WAIT)
