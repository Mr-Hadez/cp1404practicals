"""
CP1404/CP5632 - Practical
Generate quick picks
"""

import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    random_numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in random_numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_numbers.append(number)
    random_numbers.sort()
    print(" ".join(str(number) for number in random_numbers))
