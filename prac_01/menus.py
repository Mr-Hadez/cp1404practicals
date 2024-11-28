"""
CP1404 - Practical
Menu using while loop
"""

# Originally printed the menu each time, then later condensed it into a string
# variable that could be printed after seeing the solutions. Also added the
# upper() function

name = input("Enter name: ")
MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU_STRING)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>> ").upper()
print("Finished.")
