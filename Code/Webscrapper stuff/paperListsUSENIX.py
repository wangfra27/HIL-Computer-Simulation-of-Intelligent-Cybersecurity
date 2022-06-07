from typing import Text, final
from urllib.request import urlopen
import numpy as np 
import requests
import time
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

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--windowed')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--enable-javascript")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

URL = "https://www.usenix.org/search/site"
while True:
    #open google find the file
    try:
        trash = input()
    except:
        break
    title = input()
    authors = input()
    trash = input()
    trash = input()
    driver.get(URL)   
    search = driver.find_element(By.NAME, "keys")
    search.send_keys(title)
    search.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, "//ol[@class='search-results apachesolr_search-results']/li[1]/h3[1]/a[1]").click()
    driver.find_element(By.XPATH, "//span[@class='file']/a[1]").click()
    time.sleep(1)
    link = driver.current_url
    #save the file
    end = ".pdf"
    ntitle = title[:-1]

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
    response = requests.get(link)
    print(link)
    file = open(name, 'wb')
    file.write(response.content)
    file.close()
    time.sleep(1)
#move the file to the directory of choice
