"""
Example Wordpress Contact Form Code:
[contact-form]
[contact-field label='Name' type='name' required='1'/]
[contact-field label='Email' type='email' required='1'/]
[contact-field label='New Orleans Bowl 12/20/2014' type='radio' required='1' options=' Louisiana Lafayette, Nevada'/]
[/contact-form]

This generates the following look in Wordpress:
National Championship - #1 Princeton vs. #2 Yale - 1/1/1900
Options:
- Princeton
- Yale
"""
import os
import sys
from bs4 import BeautifulSoup
from lxml import html
import requests


def scrape(url):
    """
    Scrapes an ESPN URL for schedule data
    Returns an array of dictionaries containing game details
    E.g. [game{away_team, home_team, away_rank, home_rank, away_abbr, home_abbr},...]
    """
    # headers = {'User-Agent': 'Mozilla/5.0'}
    # page = requests.get(url, headers=headers)
    soup = BeautifulSoup(open('espn.html'), 'lxml')
    tables = soup.find_all('table')
    games = []
    for table in tables:
        for row in table.find_all('tr'):
            # Convert generator object to list and remove ticket details
            game_details = [item.encode('utf-8').strip() for item in row.stripped_strings][:-3]

            if 'matchup' not in game_details:  # Skip header rows
                # Normalize team info to RANK, TEAM
                if '#' not in game_details[0]:
                    game_details.insert(0, '')
                if '#' not in game_details[3]:
                    game_details.insert(3, '')
                # Just in case the  abbreviation is missing
                # ESPN is weird that way
                while len(game_details) < 6:
                    game_details.append('')

                game_dict = {}
                game_dict['away_rank'] = game_details[0]
                game_dict['away_team'] = game_details[1]
                game_dict['away_abbr'] = game_details[2]
                game_dict['home_rank'] = game_details[3]
                game_dict['home_team'] = game_details[4]
                game_dict['home_abbr'] = game_details[5]
                games.append(game_dict)
    return games

def displaySchedule(games_array):
    """
    Displays an array of dictionaries containing game details
    E.g. [game{away_team, home_team, away_rank, home_rank, away_abbr, home_abbr},...]
    Shows up as:
    away_rank   away_team   @   home_rank   home_team
    """
    for game in games_array:
        print("{:3} {:30} @ {:3} {:30}".format(game['away_rank'], game['away_team'], game['home_rank'], game['home_team']))


def main(args=None):
    url = 'http://www.espn.com/college-football/schedule'
    url = 'http://static.jsugamecocksports.com/custompages/Stats/Football/2015/teamcume.htm'
    displaySchedule(scrape(url))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
