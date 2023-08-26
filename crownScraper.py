# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 23:44:33 2023

@author: murta
"""

from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
from PIL import Image


start_time = time.time()

options = Options()
# options.add_argument("start-maximized")
options.add_argument("disable-extensions")
options.add_argument('--headless')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
    )

df = pd.read_csv('crownProds.csv')

# print(df['image'])
# this is a for loop for looping thru the different urls in the csv file
i=1
for index, row in df.iterrows():
    # print(row['image'])
    print(i)
    driver.get(row['image'])
    time.sleep(5)
    page = driver.page_source
    page_soup = soup(page,'html.parser')
    # print(page_soup)
    container=page_soup.find("section", class_="css-1h22x4r e1387xv70 wv_reveal").find_all("img", class_="css-fmei9v er6nhxj0")[1]
    # print(container['srcset'].split(',')[-1].split(' '))
    imgUrl = container['srcset'].split(',')[-1].strip().split(' ')[0]
    print(imgUrl)
    print(row['Display Name/Nick Name']+'.png')
    driver.get(imgUrl)
    imgData = requests.get(imgUrl).content
    f = open(row['Display Name/Nick Name']+'.png','wb')
    f.write(imgData)
    f.close()
    img = Image.open(row['Display Name/Nick Name']+'.png')
    # img.show()
    # if(i==3):
    #     break
    i+=1

driver.close()    
print((time.time() - start_time)/60) 