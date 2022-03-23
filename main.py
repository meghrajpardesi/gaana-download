# Utlity to play and record high quality songs 
from inspect import trace
import os 
import re
import time
import subprocess
from bs4 import BeautifulSoup 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml import etree
import pyautogui as pg

MOVIE_LIST = []


def main():
    # Initiate the browser
    browser  = webdriver.Chrome(ChromeDriverManager().install()) 

    base_url = "https://gaana.com"   
    browser.get(f"{base_url}/album/teesri-kasam")
    search_xpath = '/html/body/div[1]/header/div/div[1]/div[4]/button/span[2]'
    songs_list = f'//*[@id="app"]/main/div[2]/section[2]/div[2]'
    html = browser.page_source
    soup = BeautifulSoup(html)
    # documentObjectModel = etree.HTML(str(soup)) 
    # for i in documentObjectModel.xpath(songs_list):
    #     print(i
    songs_link = {}
    time.sleep(10)

    # for search
    # with open("bash.txt", 'w') as f:
    #     for ultag in soup.find_all('ul', {'class' : 'card_wrap'}):
    #         for litag in ultag.find_all('li',{'class':'list_card'}):
    #             songs_link[litag.text] = f"{base_url}{litag.find('a').get('href')}"
    #             s = f"python get_song.py \'{litag.text.rstrip()}\' {base_url}{litag.find('a').get('href')}"
    #             print(type(s))
    #             print(s)
    #             f.write(str(s))
    # for album
    for ultag in soup.find_all('ul', {'class' : 'list_data'}):
        for litag in ultag.find_all('li',{'class':'_wrap'}):
            songs_link[litag.text] = f"{base_url}{litag.find('a').get('href')}"
            s = f"python get_song.py \'{litag.text.lstrip()}\' {base_url}{litag.find('a').get('href')}"
            print(s)







if __name__=="__main__":
    main()