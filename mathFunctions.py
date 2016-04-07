# for any math functions that might prove useful in later projects
# or for solving Project Euler problems

import math

# Generates the Fibonacci sequence up to an upper limit
# or up to a set amount
def genFibs(limit=1000, amount=0):
    first, second = 1, 2
    fibs = [1,2]
    if amount:
        while len(fibs) != amount:
            current = first + second
            fibs.append(current)
            first = second
            second = current
        return fibs
    while True:
        current = first + second
        if current >= limit:
            break
        fibs.append(current)
        first = second
        second = current
    return fibs

# Returns the nth number in the Fibonacci sequence
def nthFib(n):
    if n <= 1:
        return n
    return (nthFib(n-1) + nthFib(n-2))

# Checks whether a number is prime
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pivot = int(math.sqrt(n))+1
    for divisor in range(3, pivot, 2):
        if n%divisor == 0:
            return False
    return True

# Generates all the prime numbers up to an upper limit
def genPrimes(limit):
    primes = list(range(2,int(limit)))
    current = 3
    while True:
        if current >= limit:
            break
        if not isPrime(current):
            if current in primes:
                primes.remove(current)
        else:
            multiples = getMultiples(primes,current)
            multiples.pop(0)
            for multiple in multiples:
                if multiple in primes:
                    primes.remove(multiple)
        current += 1
    return primes


# Finds just the even numbers in a list
def getEvens(nums):
    return [n for n in nums if n % 2 == 0]


# Finds just the odd numbers in a list
def getOdds(nums):
    return [n for n in nums if n % 2 != 0]


# Finds multiples of a number in a list
def getMultiples(nums,base):
    return [n for n in nums if n % base == 0]


# Finds the prime factorization of a number
def primeFacs(number):
    factors = []
    current = 2
    while current <= number:
        if number % current == 0:
            number /= current
            factors.append(current)
        else:
            current += 1
    factors.sort()
    return factors


# Checks whether a number is happy
def isHappy(n):
    if n == 1:
        return True
    if n == 4:
        return False
    digits = list(str(n))
    n = 0
    for digit in digits:
        digit = int(digit)
        n += digit**2
    return isHappy(n)
    

# Generates a specified amount of happy numbers
def genHappyNums(amount):
    current = 1
    happyNums = []
    while len(happyNums) != amount:
        if isHappy(current):
            happyNums.append(current)
        current += 1
    return happyNums


