import csv
from bs4 import BeautifulSoup

#firefox chrome
from selenium import webdriver
#Microsoft edge
from msedge.selenium_tools import Edge, EdgeOptions

#startup driver

#firefox and chrome
driver = webdriver.Firefox()
driver = webdriver.Chrome()
#edge
options = EdgeOptions
options.use_chromium = True
driver = Edge(options=options)

url = 'https://www.amazon.com'
driver.get(url)

def get_url(search_term):
    """Generate search term url as a string"""
    return f'https://www.amazon.com/s?k={search_term}&crid=Y2K3Z9XPV0GR&sprefix=seache%2Caps%2C949&ref=nb_sb_noss_2'
