"""
CP1404 - Practical
shop calculator with discount
"""

total_price = 0
num_item = int(input("Number of items: "))
while num_item < 0:
    print("Invalid input!")
    num_item = int(input("Number of items: "))
for i in range(num_item):
    item_price = float(input("Price of item: "))
    total_price += item_price  # Made more concise upon seeing solutions
if total_price > 100:
    total_price *= 0.9  # Same with this line
print(f"The total price for {num_item} items is ${total_price:.2f}")
