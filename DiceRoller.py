from random import randint
import time

d_size = input("How many sides are on your die? ")
d_quantity = input("How many dice will you throw? ")

min = 1
max = int(d_size)

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    diceNum = int(d_quantity)
    print("Rolling the die...")
    time.sleep(0.75)
    
    while diceNum > 0:
        the_roll = randint(min, max)
        print(the_roll)
        diceNum -= 1
    roll_again = input("Roll again? ")
