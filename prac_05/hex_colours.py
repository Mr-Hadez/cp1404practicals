"""
CP1404 Practical
Hexadecimal colour code program
"""

COLOUR_TO_CODE = {"Raspberry": "#e30b5d", "Red1": "#ff0000", "Blue1": "#0000ff", "Green1": "#00ff00",
                  "Gunmetal": "#2a3439", "MediumPurple": "#9370db", "Ash Grey": "#b2beb5",
                  "Baby Pink": "#f4c2c2", "Banana Yellow": "#ffe135", "Burnt Orange": "#cc5500"}

name = input("Enter colour name: ").title()
while name != "":
    try:
        print(f"{name} is {COLOUR_TO_CODE[name]}")
    except KeyError:
        print("Invalid colour name")
        name = input("Enter colour name: ").title()
    else:
        name = input("Enter colour name: ").title()
