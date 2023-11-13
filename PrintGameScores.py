'''
Written on Oct 5 2023 by Bradley Uppercrust III
Scores Diplomacy games with OMG scoring

to use, run the following command in the terminal:
python PrintGameScores.py <game_url> for current score
or
python PrintGameScores.py <game_url>/<year>/<season>
'''
import sys
import backstabbr_scraping as bs
from OMG_scoring import Calulate_OMG

print_territories = False
######################################################
###############   Game URL   #########################
######################################################
# game_url = 'https://www.backstabbr.com/game/Nexus-Season6-Game37/5466300639084544'
# game_url = sys.argv[1]
game_url = ""
for arg in sys.argv:
    if "backstabbr.com" in arg:
        game_url = arg

if game_url == "":
    print("Please enter a valid backstabbr game url")
    sys.exit()
######################################################
############  Get game name from URL  ################
######################################################
url_words = game_url.split("/")
# game_name = game_url.split("/")[-2]
name_index = url_words.index("game") + 1
game_name = url_words[name_index]
######################################################
########  Do the Interesting Stuff  ##################
######################################################
htmlpage = bs.fetch_and_parse(game_url)
playerTeritories = bs.territories_by_player(htmlpage)
points = Calulate_OMG(playerTeritories)
######################################################
###############  Print Results  ######################
######################################################
print("\n")
print(f"Score for {game_name}:")
for player, score in points.items():
    print(f"{player}: {score}")

if print_territories:
    print("\n")
    print("Territories By player")
    # for player, territory_dict in playerTeritories.items():
    #     print(f"{player}: {territory_dict['Territories']}")
    for player in points.keys():
        try:
            print(f"{player}: {playerTeritories[player]['Territories']}")
        except:
            print(f"{player}: 0")