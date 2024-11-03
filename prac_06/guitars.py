"""
Guitar playing program
Estimate: 15 minutes
Actual:   10 minutes
"""

from guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ")

print("These are my guitars: ")
for i, guitar in enumerate(guitars, 1):
    guitar_age = guitar.get_age()
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
