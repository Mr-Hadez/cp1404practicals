"""
Project class
"""

import datetime

class Project:
    """Project class"""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise Project constructor."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string view of Project."""
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def __repr__(self):
        """Return a string view of Project list."""
        return str(self)

    def __lt__(self, other):
        """Check if project is older than another."""
        return self.start_date < other.start_date

    def is_complete(self):
        """Check if project is complete."""
        return self.completion_percentage == 100

    def is_after_date(self, date):
        """Check if project is after a date."""
        return self.start_date >= date

