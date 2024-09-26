"""
CP1404
Amended a broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(f"Your score is {result}")
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    result = determine_score_status(random_score)
    print(f"Your score is {result}")


def determine_score_status(score):
    if 100 >= score >= 90:
        result = "Excellent"
    elif 90 > score >= 50:
        result = "Passable"
    elif 0 <= score < 50:
        result = "Bad"
    else:
        result = "Invalid score"
    return result


main()
