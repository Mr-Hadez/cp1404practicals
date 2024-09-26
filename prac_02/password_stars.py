"""
Checks password
"""


def main():
    password = get_password()
    minimum_length = 5
    while len(password) < minimum_length:
        print("Invalid input length!")
        password = get_password()
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password():
    password = input("Enter a password: ")
    return password


main()
