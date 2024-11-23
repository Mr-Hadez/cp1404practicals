"""
Taxi simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """Load menu for user to choose taxi, drive or quit."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            display_taxis(taxis)
            my_taxi = choose_taxi(taxis)
        elif choice == "D":
            pass
        else:
            print("Invalid option")
        print(f"Bill to date: ${my_taxi.get_fare()}")
        print(MENU_STRING)
        choice = input(">>> ").upper()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    taxi_choice = input("Choose taxi: ")
    my_taxi = taxis[int(taxi_choice)]
    return my_taxi


main()
