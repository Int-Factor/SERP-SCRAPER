# IMPORT LIBRARIES
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

target_urls = ['https://www.hawaiianairlines.com/',
            'https://www.horoscope.com/us/index.aspx',
            'https://www.lyst.com/',
            'https://www.dollarshaveclub.com/',
            'https://www.ralphlauren.com/',
            'https://www.logitech.com/en-in',
            'https://www.harley-davidson.com/in/en/index.html',
            'https://www.rockstargames.com/',
            'https://www.wendys.com/',
            ]


def href_lang_scraper(target_url):

    time.sleep(10)

    # CREATING SOUP
    html = requests.get(target_url)
    soup = BeautifulSoup(html.content, 'lxml')
    href_links_of_webpage = soup.find_all('link', attrs = {'rel': 'alternate'})
    
    href_lang_dict = {}

    language_codes = []

    for links in href_links_of_webpage:
        if links['href']:
            language_codes.append(links['hreflang'])
        else:
            print('hreflang not found on ' + target_url)

    ', '.join(language_codes)

    number_of_languages = len(language_codes)

    href_lang_dict['website'] = target_url
    href_lang_dict['href_lang_links'] = href_links_of_webpage
    href_lang_dict['language_codes'] = language_codes
    href_lang_dict['number_of_languages'] = number_of_languages

    return href_lang_dict

final_list_to_store_data_in = []

for url in target_urls:
    print(url)
    url_data = href_lang_scraper(url)
    final_list_to_store_data_in.append(url_data)

df = pd.DataFrame(final_list_to_store_data_in)
df.to_csv('href_lang_POC_trial.csv', index=False)