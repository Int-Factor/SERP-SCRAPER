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
import csv

#Driver related to automate browser
# GECODRIVER 
# Path = "geckodriver.exe"
# driver = webdriver.Firefox(executable_path = Path)

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

# Read column H (name) in the result_combined_200.CSV file
# read specific columns of csv file using Pandas
df = pd.read_csv("updated_result_combined_200.csv", nrows=10)
# name_column = df['updated_name']

# for i in name_column:

#     # Open Website
#     target_url = "https://www.google.com/search?q=" + i #Loop names in updated_name 
#     page = driver.get(target_url)
#     driver.maximize_window()
#     time.sleep(random.randint(10,20))


from pprint import pprint

df_as_dict_list = df.to_dict(orient='records')


def crossfit_scraper(target_url):
    return 'scraped data for ' + target_url


for i in df_as_dict_list:
    target_url = "https://www.google.com/search?q=" + i['updated_name']
    scraped_data = crossfit_scraper(target_url)
    i['scraped_data'] = scraped_data

pprint(df_as_dict_list)


# convert to dataframe and then to csv

df_new = pd.DataFrame(df_as_dict_list)
print(df_new)


