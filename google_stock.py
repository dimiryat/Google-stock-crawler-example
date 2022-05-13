# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:15:52 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

def get_web_page(url, stock_id):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/66.0.3359.181 Safari/537.36'}
    resp = requests.get(url+stock_id, headers=headers)
    if resp.status_code != 200:
        print("Invalid url: ", resp.url)
        return None
    else:
        return resp.text
    
def get_stock_info(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    stock = dict()
    
    sections = soup.find_all('g-card-section')
    
    stock['name'] = sections[1].div.text.split('>')[1]
    spans = sections[1].find_all('div', recursive=False)[1].find_all('span')
    stock['current_price'] = spans[1].text
    stock['current_change'] = spans[5].text
    
    return stock

if __name__=="__main__":
    pass
#This program can't work due to Google will prompt robot exam while running this code
#Here is just for example for reference