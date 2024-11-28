"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name):
        """Construct a band with a name."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        return "\n".join(musician.play() for musician in self.musicians)

