"""
CP1404
Amended a broken program to determine score status
"""

score = float(input("Enter score: "))

if 100 >= score >= 90:
    print("Excellent")
elif 90 > score >= 50:
    print("Passable")
elif 0 <= score < 50:
    print("Bad")
else:
    print("Invalid score")
