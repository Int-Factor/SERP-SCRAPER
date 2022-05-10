"""

    Contact Information Scraper (Generalised)

    Extracted data points:

        1. Emails
        2. Phone Numbers
        3. LinkedIn URL
        4. Facebook URL
        5. Twitter URL
        6. Instagram URL


    # TODO
        - Multi-Langauge Support
            - English
            - European Languages

        - Improve Phone Number Extraction    
"""

import re
import requests
from bs4 import BeautifulSoup, SoupStrainer

# TODO Remove later
from pprint import pprint


def get_page_source_text(url: str) -> dict:
    """returns page source and all visible text on page"""

    # For user-agent information
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)

    # Check response status
    if r.status_code == 200:
        # Page source
        page_source = r.text

        # Page visible text
        soup = BeautifulSoup(page_source, features='lxml')
        visible_text = soup.getText()

        return {'page_source': page_source, 'visible_text': visible_text}
    else:
        return None


def extract_phone_email(visible_text: str) -> dict:
    """return phone number and emails extracted from visible text"""

    # Emails
    email_matches = re.findall('[\w\.-]+@[\w\.-]+(?:\.[\w]+)+', visible_text)
    if email_matches:
        email_matches = list(set(email_matches))
    
    # Phone Numbers
    phone_matches = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", visible_text)
    if phone_matches:
        phone_matches = list(set(phone_matches))

    return {'email': email_matches, 'phone_nos': phone_matches}


def get_page_href_links(page_source):
    """returns a list of all the href links on the page"""
    href_links = []
    for link in BeautifulSoup(page_source, features='html.parser' ,parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            href_links.append(link['href'])
    
    return href_links


def identify_contact_page_url(urls):
    """returns link to the contact page"""
    contact_page_urls = []

    for url in urls:
        url = url.lower()

        words_to_find = ['contact', 'get-in-touch', 'get in touch']
        if any(ext in url for ext in words_to_find):
            contact_page_urls.append(url)
    
    if len(contact_page_urls) > 0:
        contact_page_urls.sort(key=len)
        return list(set(contact_page_urls))[0]
    else:
        return None


def extract_phone_email_contact_us_page(contact_page_url: str, base_url: str) -> dict:
    """returns emails and phone numbers from contact page"""
    if contact_page_url.startswith("http"):
        # Get page source and visuble text
        contact_page_source_and_visible_text = get_page_source_text(contact_page_url)
    else:
        index_url = base_url.rstrip('/')
        contact_page_url = contact_page_url.lstrip('/')
        target_url = base_url + '/' + contact_page_url

        contact_page_source_and_visible_text = get_page_source_text(target_url)
    
    if contact_page_source_and_visible_text:
        phone_nos_emails = extract_phone_email(contact_page_source_and_visible_text['visible_text'])
        return phone_nos_emails
    else:
        return None


def extract_social_profile_links(urls: list):
    """returns social list from a list of href/urls"""

    social_links =  {
        'linkedin': None, 
        'facebook': None, 
        'twitter': None,
        'instagram': None
    }

    for url in urls:
        url = url.lower()
        if 'twitter' in url:
            social_links['twitter'] = url
        elif 'linkedin' in url:
            social_links['linkedin'] = url
        elif 'facebook' in url:
            social_links['facebook'] = url
        elif 'instagram' in url:
            social_links['instagram'] = url
        else:
            continue
    
    return social_links



def main(url: str) -> dict:
    """Main caller"""
    
    # Get page source and visible text
    index_page_source_visible_text = get_page_source_text(url)

    if index_page_source_visible_text:
        index_page_extracted_phone_emails = extract_phone_email(index_page_source_visible_text['visible_text'])

        # Contact us page
        index_page_href_links = get_page_href_links(index_page_source_visible_text['page_source'])

         # Fetch urls for contact page
        contact_page_url = identify_contact_page_url(index_page_href_links)

        if contact_page_url:
            # Extact emails and phone nos from contact page
            contact_page_extracted_phone_emails = extract_phone_email_contact_us_page(contact_page_url, url)
        else:
            contact_page_extracted_phone_emails = 'Page Not Found'
        # Social media links
        index_social_profile_links = extract_social_profile_links(index_page_href_links)

        extracted_info = {
            'index_page_url': url,
            'contact_page_url': contact_page_url,
            'index_page_phone_emails': index_page_extracted_phone_emails,
            'contact_page_phone_emails': contact_page_extracted_phone_emails,
            'social_web_links': index_social_profile_links,
        }

        return extracted_info
    else:
        return None


if __name__ == "__main__":
    pprint(main("https://www.jessicabanxx.com"))