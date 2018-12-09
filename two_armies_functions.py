import random

def generate_army(army, soldiers, castles):
    """A function to create a randomly distributed army of 100 soldiers"""
    remaining_soldiers = soldiers
    army = []
    
    for curr_castle in range(0,castles):
    
        if remaining_soldiers == 0:
            army.append(0)

        elif remaining_soldiers >= soldiers // 2.5:
            curr_castle_deployment = random.randint(0,soldiers // 2.5)
            remaining_soldiers -= curr_castle_deployment
            army.append(curr_castle_deployment)

        else:
            curr_castle_deployment = random.randint(0,remaining_soldiers)
            remaining_soldiers -= curr_castle_deployment
            army.append(curr_castle_deployment)
                
    random.shuffle(army)
    return army

def battle_sim(army_1, army_2, castles):
    """A function to find who won the most castles on a point basis."""
    army_1_score = 0
    army_2_score = 0
    
    for castle in range(castles):
            if army_1[castle] > army_2[castle]:
                army_1_score += castle + 1
            elif army_1[castle] == army_2[castle]:
                army_1_score += (castle + 1) / 2
                army_2_score += (castle + 1) / 2
            else:
                army_2_score += castle + 1
                
    if army_1_score > army_2_score:
        return 'army_1_won'
    elif army_1_score <= army_2_score:
        return army_2_score

def multiple_battles(num_sims, total_soldiers, castles, army_1):
    """Match army_1 against many different army_2's."""
    times_won = 0
    success_rate = 0
    next_army = {
        'army': [0,0,0,0,0,0,0,0,0],
        'score': 0,
        }
    
    for sim in range(num_sims):
        army_2 = generate_army('army_2', total_soldiers, castles)
        if battle_sim(army_1, army_2, castles) == 'army_1_won':
            times_won += 1
        else:
            curr_score = battle_sim(army_1, army_2, castles)  
            if curr_score > next_army['score']:
                next_army['army'] = army_2
                next_army['score'] = curr_score
    
    success_rate = 100 * times_won / num_sims
    return success_rate, next_army
    
def add_score(userscore, high_scorelist):
   if userscore[0] > high_scorelist[len(high_scorelist)-1][0]:
       high_scorelist.append(userscore)
       high_scorelist.sort(reverse=True)
       del high_scorelist[len(high_scorelist)-1]
       return high_scorelist







