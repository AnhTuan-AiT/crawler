import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://baomoi.com/')

req = requests.get('https://baomoi.com/')
soup = BeautifulSoup(browser.page_source, "lxml")

for link in soup.find_all(class_="bm_F"):
    num_related_articles = int(link.get_text().replace(" liên quan", ""))
    if 1 < num_related_articles < 30:
        print(link.get('href') + ": " + str(num_related_articles))
