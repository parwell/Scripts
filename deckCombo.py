# generates random pairings of colors in Magic: the Gathering

import random
import sys


def generateCombos():
    combos = []
    decks = ['W','L','B','R','G']
    for i, c1 in enumerate(decks):
        for c2 in decks[i+1:]:
            combo = c1 + c2
            combos.append(combo)
    return combos


def displayCombos():
    combos = generateCombos()
    random.shuffle(combos);
    for combo in combos:
	    print(combo)

		
def main():
    displayCombos()
    input()

	
if __name__ == '__main__':
    main()
    sys.exit()
