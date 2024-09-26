"""
Checks password
"""

password = input("Enter a password: ")
minimum_length = 5
while len(password) < minimum_length:
    print("Invalid input length!")
    password = input("Enter a password: ")
print("*" * len(password))
