"""
CP1404
Amended a broken program to determine score status and generate random score
"""

import random


def main():
    """Get score, determine status and generate random score."""
    score = int(input("Enter score: "))
    result = determine_score_status(score)
    print(f"{result}")
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    result = determine_score_status(random_score)
    print(f"Your score is {result}")


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


if __name__ == "__main__":
    main()
