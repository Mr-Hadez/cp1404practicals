"""
CP1404
Generate random scores and evaluate them
"""

import random


def main():
    """Get score, determine status and generate random score."""
    number_of_scores = int(input("Enter number of random scores to be generated: "))
    for i in range(number_of_scores):
        random_score = random.randint(0, 100)
        result = determine_score_status(random_score)
        print(f"{random_score} is {result}")


def determine_score_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
