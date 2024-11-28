"""
CP1404/CP5632 Practical
Program to read all of these guitars and store them in a list of Guitar objects
"""

from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read file of guitars, save as objects, display."""
    guitars = []

    load_data(guitars)
    get_input(guitars)
    save_data(guitars)
    display_guitars(guitars)


def save_data(guitars):
    with open(FILENAME, "w", newline="") as out_file:
        for guitar in guitars:
            print(guitar, file=out_file)


def display_guitars(guitars):
    """Display all guitars sorted from oldest to newest."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_input(guitars):
    """Get user input until blank input is entered."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")


def load_data(guitars):
    """Read data from file and store in list of Guitar objects."""
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), parts[2])
            guitars.append(guitar)


main()
