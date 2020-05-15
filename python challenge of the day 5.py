import random

def five():
    random_list = random.sample(range(100, 201, 2), 5)

    return random_list

print(five())
