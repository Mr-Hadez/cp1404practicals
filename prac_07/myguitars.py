"""
CP1404/CP5632 Practical
Program to read all of these guitars and store them in a list of Guitar objects
"""

import csv
from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read file of guitars, save as objects, display."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

main()

