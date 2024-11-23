"""
Taxi simulator
"""

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """Load menu for user to choose taxi, drive or quit."""
    print("Let's drive!")
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            pass
        elif choice == "D":
            pass
        else:
            print("Invalid option")
        print(MENU_STRING)
        choice = input(">>> ").upper()


main()
