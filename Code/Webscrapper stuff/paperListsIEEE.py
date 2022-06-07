from typing import Text, final
from urllib.request import urlopen
from bs4.element import ProcessingInstruction
import numpy as np 
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from urllib3.packages.six import b
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
import shutil

download_dir = "C:\\Users\\frank\\Documents\\papers"
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--enable-javascript")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

URL = "https://www.computer.org/csdl/proceedings/sp/2022/1wKCdeg89vq"
first = True
while True:
    #open website find the file
    try:
        title = input()
    except:
        break
    authors = input()
    driver.get(URL)   
    search = driver.find_element(By.NAME, "basicSearchText")
    search.send_keys(title)
    search.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, "//a[@class='article-title']").click()
    driver.find_element(By.XPATH, "//div[@class='article-action-toolbar mt-3']/a[1]").click()
    link = driver.current_url
    #save the file
    response = urllib.request.urlopen(link) 
    #edit name of file(filenames cant have ", ?, : so this just finds those and deletes them
    end = ".pdf"
    ntitle = title[:-2]

    location = ntitle.find('"')
    while (location != -1):
        ntitle = ntitle[:location] + ntitle[location + 1:]
        location = ntitle.find('"')
    
    location = ntitle.find(':')
    while (location != -1):
        ntitle = ntitle[:location] + ntitle[location + 1:]
        location = ntitle.find(':')
    
    location = ntitle.find('?')
    while (location != -1):
        ntitle = ntitle[:location] + ntitle[location + 1:]
        location = ntitle.find('?')

    name = ntitle + end
    print(name)
    #save the file its meant to do that by copying the data
    file = open(name, 'wb')
    file.write(response.content())
    file.close()
    #a sleep to not break the website and then it closes the tab since this one opens a new tab
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
#move the file to the directory of choice