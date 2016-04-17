# Bogosort
import random

def bogoSort(a, b):
    a = list(a.lower())
    b = list(b.lower())
    iterations = 0
    while a != b:
        iterations += 1
        random.shuffle(b)
    return iterations

for i in range(10):
    print(bogoSort("qwerty", "ytrewq"))

input()
        
