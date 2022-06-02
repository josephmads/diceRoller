from random import randint as roll
import time

def diceroller(size, quantity):
  for n in range(quantity):
    dice = roll(1, size)
    print(dice)

setup_dice = True

while setup_dice == True:
    d_size = int(input("How many sides are on your dice?: "))
    d_quantity = int(input("How many dice will you throw?: "))

    rolling = True

    while rolling == True:
        print("Rolling the dice...")
        time.sleep(0.75)
        diceroller(d_size, d_quantity)
        
        roll_again = input("Roll [a]gain, Roll [n]ew dice, or [q]uit?: ")
        if roll_again == "a":
            continue
        if roll_again == "n":
            rolling = False
            continue
        if roll_again == "q":
            rolling = False
            setup_dice = False
            break

