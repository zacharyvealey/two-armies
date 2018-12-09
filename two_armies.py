###############################################################################
#                                                                             #
#  A program that simulates how individual armies fare at obtaining the most  #
#                         number of castle points.                            #
#                                                                             #
###############################################################################

import random
import two_armies_functions as af

# Initialize number of castles, total soldiers, amount of times one army faces
# off against a number of other random armies, how many simulations of that 
# number of wars, and the interval at which you want to see the high score list.
castles = 10
total_soldiers = 100
num_wars = 1000
num_iterations = 400
high_score_interval = 50
high_scorelist = [(0,[0,0,0,0,0,0,0,0,0])]*5

def run_simulation():
    for i in range(num_iterations):
        if i == 0:
            army_1 = af.generate_army('army_1', total_soldiers, castles)
            success_rate, next_army = af.multiple_battles(num_wars, total_soldiers, castles, army_1)
            userscore = (success_rate, army_1)
            af.add_score(userscore, high_scorelist)

        elif i % high_score_interval == 0:
            army_1 = next_army['army']
            success_rate, next_army = af.multiple_battles(num_wars, total_soldiers, castles, army_1)
            userscore = (success_rate, army_1)
            af.add_score(userscore, high_scorelist)
            
            for score in high_scorelist:
                print(str(score[1]) + "\t" + str(score[0]) + "%")
            print("\n")
            
        else:
            army_1 = next_army['army']
            success_rate, next_army = af.multiple_battles(num_wars, total_soldiers, castles, army_1)
            userscore = (success_rate, army_1)
            af.add_score(userscore, high_scorelist)
            
    # Final high scores.
    for score in high_scorelist:
        print(str(score[1]) + "\t" + str(score[0]) + "%")
        
# Run the simulation.
run_simulation()


