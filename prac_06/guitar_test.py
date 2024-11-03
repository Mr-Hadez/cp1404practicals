"""
Guitar testing program
Estimate: 10 minutes
Actual:   10 minutes
"""

from guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035)
another_guitar = Guitar("Another Guitar", 2013, 16035)

print(f"Gibson L-5 CES get_age() - Expected 100. Got {guitar.get_age()}")
print(f"Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
