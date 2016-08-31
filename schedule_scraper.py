"""
Web Scraper to Get Schedule
"""
import os
import sys
from bs4 import BeautifulSoup
from lxml import html
import requests

def scrape(url):
    # headers = {'User-Agent': 'Mozilla/5.0'}
    # page = requests.get(url, headers=headers)
    soup = BeautifulSoup(open('espn.html'), 'lxml')
    tables = soup.find_all('table')
    for table in tables:
        for row in table.find_all('tr'):
            print([string for string in row.stripped_strings])
    return tables

def main(args=None):
    url = 'http://www.espn.com/college-football/schedule'
    url = 'http://static.jsugamecocksports.com/custompages/Stats/Football/2015/teamcume.htm'
    scrape(url)
    # print(team.prettify())

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
