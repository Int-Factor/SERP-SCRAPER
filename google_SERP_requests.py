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
import requests
import csv


# utilites functions
def bot_random_sleep():
    """sleep for random time"""
    x = random.randint(3,7)
    time.sleep(x)

# Read column H (name) in the result_combined_200.CSV file
# read specific columns of csv file using Pandas
df = pd.read_csv("updated_result_combined_200.csv", nrows=4)

from pprint import pprint
df_as_dict_list = df.to_dict(orient='records')


def google_crossfit_scraper(target_url):
    
    html = requests.get(target_url)
    soup = BeautifulSoup(html,'lxml')

    main_div = soup.find('div', attrs = {'id' : 'center_col' , 'class' : 's6JM6d'})
    required_divs = main_div.find_all('div', attrs = {'class' : 'tF2Cxc'})

    # CREATE EMPTY LIST TO STORE STUFF
    serp_data_page_1 = []

    for items in required_divs:

        urls = items.find('div', attrs = {'class' : 'yuRUbf'})(href=True)
        for x in urls:
            req_urls = x['href']
        
        page_name = items.find('h3', attrs ={'class' : 'LC20lb MBeuO DKV0Md'})
        description = items.find('div', attrs = {'class' : 'lEBKkf'})
        
        print(req_urls)
        print(page_name.text)
        print(description.text)
        
        temp_dict = {}
        
        # saving these in the dictionary
        temp_dict['url'] = req_urls
        temp_dict['webpage_name'] = page_name.text
        temp_dict['description'] = description.text
        
        serp_data_page_1.append(temp_dict)

        return serp_data_page_1

for i in df_as_dict_list:
    time.sleep(random.randint(10,15))

    target_url = i['google_url']
    scraped_data = google_crossfit_scraper(target_url)
    i['scraped_data'] = scraped_data

pprint(df_as_dict_list)

# convert to dataframe and then to csv
df_new = pd.DataFrame(df_as_dict_list)
print(df_new)
