"""Guitar class"""


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise Guitar constructor"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """..."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self, current_year):
        """Calculate the age of the guitar"""
        return current_year - self.year

    def is_vintage(self, age):
        """Determine if the guitar is vintage"""
        return age >= 50
