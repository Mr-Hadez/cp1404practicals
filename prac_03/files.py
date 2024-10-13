"""
CP1404/CP5632 - Practical
Answer questions to understand different ways to read files
"""

# 1
username = input("Enter your name: ")
out_file = open("name.txt", "w")
print(username, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3
with open("numbers.txt", "r") as in_file:
    number_1 = in_file.readline().strip()
    number_2 = in_file.readline().strip()
    total_number = int(number_1) + int(number_2)
    print(total_number)

# 4
with open("numbers.txt", "r") as in_file:
    total_number = 0
    for line in in_file:
        total_number += int(line.strip())
    print(total_number)