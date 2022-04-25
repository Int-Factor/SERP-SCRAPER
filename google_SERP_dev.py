"""
    Scraper to scrape Google SERP 
    SERP = Search Engine Results Page
    
    Steps - 
    1. Open Google
    2. Enter Keywords
    3. Fetch results
    4. Scrape Data (URL, Headline, Description)
    5. Save to CSV.
"""

# IMPORT LIBRARIES
import sys
import time
from time import sleep
import random
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys


#Driver related to automate browser
# GECODRIVER 
Path = "geckodriver.exe"
driver = webdriver.Firefox(executable_path = Path)

'''WRITE THIS FOR RUNNING GECKODRIVER IN HEADLESS MODE'''

# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)

'''HEADLESS CODE ENDS HERE'''

# utilites functions
def bot_random_sleep():
    """sleep for random time"""
    x = random.randint(3,7)
    time.sleep(x)

user_input = input('Type crossfit gym name : ')
add = user_input.replace(' ', '+')


# Open Website
target_url = "https://www.google.com/search?q=" + add
page = driver.get(target_url)
driver.maximize_window()

