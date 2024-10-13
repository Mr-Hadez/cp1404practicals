"""
CP1404/CP5632 - Practical
List exercises
"""

# Basic list
numbers = []
number_index = 1

number = int(input(f"Number {number_index}: "))
while number >= 0:
    numbers.append(number)
    number_index += 1
    number = int(input(f"Number {number_index}: "))
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
