import random

def throwDice(number_of_dice):
    dice = []
    
    for i in range(number_of_dice):
        dice.append(random.randint(1,6))

    return dice