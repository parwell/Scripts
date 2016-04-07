import sys

def collatz(number):
    if number % 2 == 0:
        return number / 2
    return (number * 3) + 1

def countSteps(number):
    steps = 0
    print(int(number), end=" ")
    while number != 1:
        steps += 1
        number = collatz(number)
        print(int(number), end=" ")
    return steps

def getInput():
    answer = input("Enter positive integer (enter to quit): ")
    if answer:
        try:
            number = int(answer)
            if number > 0:
                displayResult(countSteps(number))
            else:
                print("Only works for positive integers.")
        except:
            print("Invalid input.")
        getInput()

def displayResult(steps):
    print("\nSteps to get to one: " + str(steps))

def run():
    print("Collatz Conjecture Checker.")
    getInput()

if __name__ == '__main__':
    run()
    sys.exit()