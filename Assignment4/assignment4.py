import requests as r
from bs4 import BeautifulSoup
import time

already_scraped = []


def get_rnlp(filename):
    base_url = 'http://reynoldsnlp.com/scrape/'
    new_url = base_url + filename
    headers = {'user-agent': 'Peter Garrow (garrowp@byu.edu)'}
    response = r.get(new_url, headers)
    path = 'scrape/' + filename
    with open(path, 'w') as my_file:
        print(response.text, file=my_file)


def get_href(filename):
    path = 'scrape/' + filename
    with open(path, 'r') as my_file:
        soup = BeautifulSoup(my_file, 'html.parser')
        a_tags = soup.findAll('a')
        for a in a_tags:
            href = a['href']
            file = href.split('/')[-1]
            if file not in already_scraped:
                get_rnlp(file)
                already_scraped.append(file)
                get_href(file)
                time.sleep(2)

get_rnlp("aa.html")
get_href("aa.html")
