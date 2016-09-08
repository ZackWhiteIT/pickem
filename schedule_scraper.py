"""
Scrapes an ESPN URL for schedule data
Returns an array of dictionaries containing game details
E.g. [game{away_team, home_team, away_rank, home_rank, away_abbr, home_abbr},...]

Displays dictionary as in a terminal as...

    South Dakota State             @ #13 TCU
    Stephen F Austin               @     Texas Tech
    New Hampshire                  @     San Diego State
#2  Clemson                        @     Auburn
    BYU                            @     Arizona
    Northern Illinois              @     Wyoming
    Northern Arizona               @     Arizona State
#10 Notre Dame                     @     Texas
#11 Ole Miss                       @ #4  Florida State
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
    """
    # headers = {'User-Agent': 'Mozilla/5.0'}
    # page = requests.get(url, headers=headers)
    soup = BeautifulSoup(open('espn.html'), 'lxml')
    tables = soup.find_all('table')
    games = []
    for table in tables:
        for row in table.find_all('tr'):
            # Convert generator object to list and remove ticket details
            game_details = [str(item) for item in row.stripped_strings][:-3]

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

def displaySchedule(games_array, output_type):
    """
    Displays an array of dictionaries containing game details
    E.g. [game{away_team, home_team, away_rank, home_rank, away_abbr, home_abbr},...]
    Shows up as:
    away_rank   away_team   @   home_rank   home_team
    If output type is CSV:
    home_rank,home_team,away_rank,away_team
    """
    if output_type == 'csv':
        for game in games_array:
            print("{},{},{},{}".format(game['home_rank'], game['home_team'], game['away_rank'], game['away_team']))
    else:
        for game in games_array:
            print("{:3} {:30} @ {:3} {:30}".format(game['away_rank'], game['away_team'], game['home_rank'], game['home_team']))


def main(args=None):
    url = 'http://www.espn.com/college-football/schedule'
    url = 'http://static.jsugamecocksports.com/custompages/Stats/Football/2015/teamcume.htm'
    displaySchedule(scrape(url), 'csv')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
