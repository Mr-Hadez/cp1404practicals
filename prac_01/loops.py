"""
CP1404 - Practical
Pracice using loops
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Question b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Question c
num_of_stars = int(input("Number of stars: "))
for i in range(num_of_stars):
    print("*", end='')
print()

# Question d
# I originally had two for loops, then I condensed it down to one after seeing
# the solutions.
for i in range(1, num_of_stars + 1):
    print("*" * i)
print()
