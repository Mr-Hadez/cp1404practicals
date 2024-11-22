"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name):
        """Construct a band with a name."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a band to the band."""
        self.musicians.append(musician)