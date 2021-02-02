from bs4 import BeautifulSoup
import requests
import re
from app.helpers import save_results

def task_handler(url):
    page_source = requests.get(url).text
    filtered_page_source = only_embeds_with_a_letter(page_source)
    save_results(filtered_page_source, url)

def only_embeds_with_a_letter(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    for t in soup.findAll(text=True):
        if "a" not in t:
            t.extract()
    return str(soup)
