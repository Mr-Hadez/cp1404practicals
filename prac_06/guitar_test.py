"""Guitar testing program"""

from guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035)
another_guitar = Guitar("Another Guitar", 2013, 16035)
guitar_age = guitar.get_age(2022)
another_guitar_age = another_guitar.get_age(2022)
is_guitar_vintage = guitar.is_vintage(guitar_age)
is_another_guitar_vintage = guitar.is_vintage(another_guitar_age)
print(f"Gibson L-5 CES get_age() - Expected 100. Got {guitar_age}")
print(f"Another Guitar get_age() - Expected 9. Got {another_guitar_age}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {is_guitar_vintage}")
print(f"Another Guitar is_vintage() - Expected False. Got {is_another_guitar_vintage}")
