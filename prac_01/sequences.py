"""
CP1404
Menu-driven number sequence generator
"""
x = int(input("Enter x: "))
y = int(input("Enter y: "))
MENU_STRING = """1. Show the even numbers from x to y\n
2. Show the odd numbers from x to y\n
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n
4. Exit the program"""
print(MENU_STRING)
choice = int(input(">>> "))
while choice != 4:
    if choice == 1:
        if x % 2 != 0:
            x += 1
        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
    elif choice == 2:
        if x % 2 == 0:
            x += 1
        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
    elif choice == 3:
        for i in range(x, y + 1):
            print(i ** 2, end=' ')
        print()
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = int(input(">>> "))
print("Finished.")
