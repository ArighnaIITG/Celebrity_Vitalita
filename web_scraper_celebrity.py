# @Author : Arighna Chakrabarty

# This program scrapes the data of celebrities born on a particular date, from the webpage of IMDB
# and displays it on a website.

from selenium import webdriver           # Imports webdriver from selenium package
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome()              # Uses Google Chrome as your webDriver

driver.get = ("http://m.imdb.com/feature/bornondate")

html = driver.page_source
driver.close()

soup = bs(html, 'html5lib')