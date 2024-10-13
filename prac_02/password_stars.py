"""
Checks password and prints stars for each letter in the password
"""


def main():
    """Get password, check for valid length and print stars using functions."""
    password = get_password()
    print_stars(password)


# Moved all password checking to function after seeing solution
def get_password():
    """Get password and check for valid length"""
    password = input("Enter a password: ")
    minimum_length = 5
    while len(password) < minimum_length:
        print("Invalid input length!")
        password = get_password()
    return password


def print_stars(password):
    """Print stars for each letter in password."""
    print("*" * len(password))


main()
