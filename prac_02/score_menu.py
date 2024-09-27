"""
Print stars for score
"""

from score import determine_score_status

MENU_STRING = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_status(score)
            print(f"{result}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Enter score: "))
    while score <= 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


main()
