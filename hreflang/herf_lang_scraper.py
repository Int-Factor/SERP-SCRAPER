# IMPORT LIBRARIES
import pandas as pd
from bs4 import BeautifulSoup
import requests


target_url = 'https://www.lyst.com/'
# 'https://www.dollarshaveclub.com/'
# 'https://www.ralphlauren.com/'
# 'https://www.logitech.com/en-in'
# 'https://www.harley-davidson.com/in/en/index.html'

html = requests.get(target_url)
soup = BeautifulSoup(html.content, 'lxml')

links_of_webpage = soup.find_all('link', attrs = {'rel': 'alternate'})

print(links_of_webpage)