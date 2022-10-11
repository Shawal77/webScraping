from bs4 import BeautifulSoup
import requests

DEFAULT_SORT = ''
NEWEST_SORT = '&sort=newest#catalog-listing'
LOW_PRICE_SORT = '&sort=lowest-price#catalog-listing'
HIGH_PRICE_SORT = '&sort=highest-price#catalog-listing'
RATING_SORT = '&sort=rating#catalog-listing'

class Article:
    def __init__(self,price:str,name:str,star:str,link:str) -> None:
        self.name = name
        self.price = price
        self.stars = star
        self.link = link

QUERY_ITEM = 'jacket'#input('What do you want to search')
sort_criterion = LOW_PRICE_SORT#input???
JUMIA_QUERY_URL = f'https://www.jumia.ug/catalog/?q={QUERY_ITEM}{sort_criterion}'
HTML_DATA = requests.get(JUMIA_QUERY_URL).text

soup = BeautifulSoup(HTML_DATA,'lxml')

articles = soup.find_all('article',class_="prd _fb col c-prd")
for article in articles:
    item_price = article.find('div',class_="prc").text
    item_name = article.find('h3',class_="name").text
    try:item_stars = article.find('div',class_="rev").text
    except:item_stars = 'X'
    item_link = article.a['href']

    print(f'\n{item_name}\n{item_price}\n{item_stars}\n{item_link}')

























#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#options = webdriver.ChromeOptions()
#service = ChromeService(executable_path='ENTER YOUR PATH TO CHROMEDRIVER')
#driver = webdriver.Chrome(service=service, options=options)
#driver.get('https://www.jumia.com.ng/catalog/?q=oraimo&shipped_from=country_local&page=1#catalog-listing')

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-list="sponsored"]')))

#soup = BeautifulSoup(driver.page_source, 'lxml')

#print([x.text for x in soup.select('article h3.name')])

#driver.close()

