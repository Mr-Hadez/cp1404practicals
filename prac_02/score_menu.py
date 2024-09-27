"""
Print stars for score
"""

from score import determine_score_status

MENU_STRING = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
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


main()
