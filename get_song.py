# Utlity to play and record high quality songs 
import sys
from inspect import trace
import os 
import time
import subprocess
from bs4 import BeautifulSoup 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml import etree
import pyautogui as pg

def main(song, link):
    browser = webdriver.Chrome(ChromeDriverManager().install()) 
    time.sleep(3)
    print("="*80, link)
    
    browser.get(link)
    time.sleep(6)
    print("="*80)
    browser.find_element(by=By.XPATH, value='//*[@id="playBtn1"]').send_keys(Keys.ENTER)

    time.sleep(4)
    song_length = browser.find_element(by=By.XPATH, value='//*[@id="detail_info"]/div[3]/div[3]/span[3]').text
    song_length = int(song_length.split(' ')[0])*60 + int(song_length.split(' ')[2])+5
    recorder_command  = ["ffmpeg", "-f", "pulse", "-i", "4", "-ac", "2", f"{song.lstrip()}.mp3", "-y",]

    time.sleep(5)

    pg.click(471,436, interval=0.5)
    pg.click(471,436, interval=9)
    
    subprocess.run(recorder_command, timeout=song_length,)
  
    # pg.click(471,436)
    time.sleep(song_length)

if __name__=='__main__':
    song_name = sys.argv[1]
    song_link = sys.argv[2]
    main(song_name, song_link)