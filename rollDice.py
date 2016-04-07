# dice roller

import random
import sys


def rollDie(faces):
    roll = random.randrange(0,faces) + 1
    return roll

	
def rollDice(dice, faces):
    rolls = []
    for i in range(dice):
        roll = rollDie(faces)
        rolls.append(roll)
    return rolls

	
def parseInput(text):
    numbers = []
    text = text.lower()
    try:
	    print("trying")
        numbers = text.split('d')
        numbers[0] = int(numbers[0])
        numbers[1] = int(numbers[1])
    except:
	    print("excepting")
        print("\nInvalid input.\n")
        return 0
    print("out of try/except")
	print("returning " + numbers)
    return numbers


def getRolls():
    numbers = parseInput(getInput())
    if numbers != 0:
        dice = numbers[0]
        faces = numbers[1]
        rolls = rollDice(dice, faces)
        return rolls
    return 0


def displayRolls():
    rolls = getRolls()
    if rolls != 0:
        print("Rolls: ", end='')
        for roll in rolls:
            print(roll, end=' ')

def getInput():
	rolls = input("Enter rolls (enter to quit): ")
	return rolls


def run():
    print("Dice Roller")
    rolls = getRolls()
    while rolls:
            displayRolls()
            rolls = getRolls()
    input("\n\nGood-bye.\n\n")


if __name__ == '__main__':
    run()
    sys.exit()