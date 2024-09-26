"""
CP1404 - Practical
Sales bonus calculator using while loop
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 0.10
    else:
        bonus = 0.15
    total_bonus = (sales * bonus)
    print(f"Bonus is: ${total_bonus}")
    sales = float(input("Enter sales: $"))
