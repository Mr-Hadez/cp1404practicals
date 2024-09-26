"""
CP1404
Amended a broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
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
