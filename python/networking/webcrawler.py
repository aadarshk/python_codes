#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    while page <= max_pages:
        url = "http://mangafox.me/directory/"+str(page)+"2.htm"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for line in soup.findAll('a',{'class':'title'}):
            href = line.get('href')
            title = line.string
            print(href)
            print(title)
        page += 1

trade_spider(1)
