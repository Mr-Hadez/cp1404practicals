"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. ValueError will occur when the numerator or denominator is not a valid integer, such as if a float is typed in or a string.
# 2. A ZeroDivisionError will occur when the denominator is zero.
# 3. You could have a while loop that checks if the denominator equals zero and asks the user to type a valid number until it is not a zero.
