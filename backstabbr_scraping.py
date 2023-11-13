'''
Written  on Oct 5 2023 by Bradley Uppercrust II
For extracting info from backstabbr.com
'''
import requests
from bs4 import BeautifulSoup
import re
import json
### These could in theory change with backstabbr updates ###
territorystring = "var territories = "
unitsstring = "var unitsByPlayer = "
#############################################################

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to fetch {url}")
    

def extract_units(html):
    regex_pattern = f"{unitsstring}(\{{.*\}});"
    # Find the script tag containing the JSON data
    # script_tag = html.find('script', text=re.compile(r'var unitsByPlayer ='))
    script_tag = html.find('script', text=re.compile(regex_pattern))

    if script_tag:
        # Extract the JSON data from the script
        # json_data = re.search(r'var unitsByPlayer = (\{.*\});', script_tag.string)
        json_data = re.search(regex_pattern, script_tag.string)
        if json_data:
            units_by_player = json.loads(json_data.group(1))
            
            # Extract supply center information
            supply_centers = {}
            for player, territories_owned in units_by_player.items():
                supply_centers[player] = len(territories_owned)
            
            return supply_centers

    return {}

def extract_territories(html):
    '''
    returns a dictionary of territories as keys and the player as values
    '''
    regex_pattern = f"{territorystring}(\{{.*\}});"
    # Find the script tag containing the JSON data
    script_tag = html.find('script', text=re.compile(regex_pattern))
    if script_tag:
        # Extract the JSON data from the script
        json_data = re.search(regex_pattern, script_tag.string)
        if json_data:
            territories = json.loads(json_data.group(1))
            return territories

def territories_by_player(html):
    '''
    returns a dictionary of players as keys with a list of territories as values
    ex { 'Austria': {
        'Territories': 3,
        'Owned': ['Budapest', 'Trieste', 'Vienna']
        },
    'England': {
        'Territories': 4,
        'Owned': ['Edinburgh', 'Liverpool', 'London', 'Norway'],']}
        }
    '''
    territories = extract_territories(html)
    territories_by_player = {}
    for territory, player in territories.items():
        if player in territories_by_player:
            territories_by_player[player]['Owned'].append(territory)
        else:
            territories_by_player[player] = { 'Territories': 0, 'Owned': [territory]}
    # for territory, player in territories.items():
    #     if player in territories_by_player:
    #         territories_by_player[player].append(territory)
    #     else:
    #         territories_by_player[player] = [territory]
    for player, territory_dict in territories_by_player.items():
        territory_dict['Territories'] = len(territory_dict['Owned'])
    return territories_by_player
