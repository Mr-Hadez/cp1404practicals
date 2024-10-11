"""
CP1404/CP5632 - Practical
Generate quick picks
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    numbers = []
    for j in range(0, 6):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(number)
    numbers.sort()
    print(" ".join(str(number) for number in numbers))