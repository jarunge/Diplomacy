'''
Written by Bradley Uppercrust III Oct 5 2023
For OMG Scoring of Diplomacy
'''


Points={
    "Austria":0,
    "England":0,
    "France":0,
    "Germany":0,
    "Italy":0,
    "Russia":0,
    "Turkey":0
}

def is_solo(territories:dict):
    '''
    checks if player received a solo victory
    '''
    for player, territory_dict in territories.items():
        if territory_dict['Territories'] >= 18:
            return player
    return False

def solo_points(points:dict,solo:str):
    '''
    returns a dictionary of points for each player
    '''
    # solo = is_solo(territories)
    # points = {}
    if solo:
        # points = {}
        # for player, territory_dict in territories.items():
        for player in points.keys():
            if player == solo:
                points[player] = 100
            else:
                points[player] = 0
        return points
    else:
        return False
    
def top_scores(territories:dict):
    '''
    returns a dictionary of the top 3 scores
    '''
    winners = {
        'first':{'territories':0, 'players':[]},
        'second':{'territories':0, 'players':[]},
        'third':{'territories':0, 'players':[]}
    }
    for player, territory_dict in territories.items():
        if territory_dict['Territories'] > winners['first']['territories']:
            winners['third']['territories'] = winners['second']['territories']
            winners['third']['players'] = winners['second']['players']
            winners['second']['territories'] = winners['first']['territories']
            winners['second']['players'] = winners['first']['players']
            winners['first']['territories'] = territory_dict['Territories']
            winners['first']['players'] = [player]
        elif territory_dict['Territories'] == winners['first']['territories']:
            winners['first']['players'] .append(player)
        elif territory_dict['Territories'] > winners['second']['territories']:
            winners['third']['territories'] = winners['second']['territories']
            winners['third']['players'] = winners['second']['players']
            winners['second']['territories'] = territory_dict['Territories']
            winners['second']['players'] = [player]
        elif territory_dict['Territories'] == winners['second']['territories']:
            winners['second']['players'] .append(player)
        elif territory_dict['Territories'] > winners['third']['territories']:
            winners['third']['territories'] = territory_dict['Territories']
            winners['third']['players'] = [player]
        elif territory_dict['Territories'] == winners['third']['territories']:
            winners['third']['players'] .append(player)
    return winners

def determine_winners(territories:dict):
    '''rearranges the winners so the right people will get points'''
    winners = top_scores(territories)
    firstplaces = len(winners['first']['players'])
    secondplaces = len(winners['second']['players'])
    if firstplaces > 1:
        winners['third'] = winners['second']
        winners['second'] = winners['first']
        if firstplaces > 2:
            winners['third'] = winners['first']
    elif secondplaces > 1:
        winners['third'] = winners['second']
    return winners
        
def award_first_place(points:dict,winners:dict):
    points_per_player = 4.5/len(winners['first']['players'])
    for player in winners['first']['players']:
        points[player] += points_per_player
    return points

def award_second_place(points:dict,winners:dict):
    points_per_player = 3/len(winners['second']['players'])
    for player in winners['second']['players']:
        points[player] += points_per_player
    return points

def award_third_place(points:dict,winners:dict):
    points_per_player = 1.5/len(winners['third']['players'])
    for player in winners['third']['players']:
        points[player] += points_per_player
    return points

def omg_bonus_points(points:dict,winners:dict):
    '''
    returns a dictionary of points for each player
    first place gets 4.5 poins
    second place gets 3 points
    third place gets 1.5 points
    '''
    points = award_first_place(points,winners)
    points = award_second_place(points,winners)
    points = award_third_place(points,winners)
    return points

def Apply_Bonus_Points(points:dict,territories:dict):
    '''
    returns a dictionary of points for each player
    first determine who gets 1st, 2nd, and 3rd place
    '''
    winners = determine_winners(territories)
    points = omg_bonus_points(points,winners)
    return points

def omg_tribute(points:dict,territories:dict):
    '''
    returns a dictionary of points for each player
    applys the tribute rule of omg scoring:
    each player gives to the board topper the smaller of 
    (0.5 the players score) & (1st place Centers - 2nd place Centers)
    '''
    winners = top_scores(territories)
    assert len(winners['first']['players']) == 1
    tribute = winners['first']['territories'] - winners['second']['territories']
    winner = winners['first']['players'][0] # only one player in first place
    for player in points.keys():
        # if player != winner: # dont need
        paid = min(0.5 * points[player],tribute)
        points[player] -= paid
        points[winner] += paid
    return points

def Apply_Tribute(points:dict,territories:dict):
    '''
    returns a dictionary of points for each player
    '''
    winners = top_scores(territories)
    if len(winners['first']['players']) == 1:
        points = omg_tribute(points,territories)
    return points

def Calulate_OMG(territories:dict):
    points = Points.copy()
    ###  First see if there is a solo
    solo = is_solo(territories)
    if solo:
        return solo_points(points,solo)
    # if not, then calculate points
    ## a) 9 points for surviving
    for player in territories.keys():
        if territories[player]['Territories'] > 0:
            points[player] += 9
    ## b) Calculate the number of supply centers owned by each player
    for player, territory_dict in territories.items():
        points[player] += 1.5 * territory_dict['Territories']
    ## c) Bonus points for being in the top 3
    points = Apply_Bonus_Points(points,territories)
    ## d) Apply Tribute
    points = Apply_Tribute(points,territories)
    return points



