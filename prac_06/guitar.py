"""
Guitar class
Estimate: 5 minutes
Actual:   5 minutes
"""

VINTAGE_AGE = 50
CURRENT_YEAR = 2022


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise Guitar constructor"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string view of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
