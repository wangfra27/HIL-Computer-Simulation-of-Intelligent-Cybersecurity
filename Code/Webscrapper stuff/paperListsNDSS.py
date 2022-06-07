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

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--enable-javascript")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

URL = "https://www.google.com/"
while True:
    #open google find the file
    try:
        title = input()
    except:
        break
    authors = input()
    driver.get(URL)
    ndss = " ndss"
    gsearch = title + ndss
    search = driver.find_element(By.NAME, "q")
    search.send_keys(gsearch)
    search.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, "//div[@class='yuRUbf']/a[1]").click()
    driver.find_element(By.XPATH, "//div[@class='btn-group-vertical']/a[1]").click()
    link = driver.current_url
    #save the file

    end = ".pdf"
    ntitle = title

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
    response = requests.get(link)
    with open(name, 'wb') as f:
        f.write(response.content)
    f.close()
    time.sleep(1)
#move the file to the directory of choice

