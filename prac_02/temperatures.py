"""
CP1404 - Practical
temperature conversion with functions
"""

MENU_STRING = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    """Convert temperatures from Celsius to Fahrenheit or vice versa."""
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} F")
        else:
            print("Invalid option")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calculate_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
