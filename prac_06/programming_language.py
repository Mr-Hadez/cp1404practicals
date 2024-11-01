"""Programming languages class"""

class ProgrammingLanguage:
    """Programming languages class"""

    def __init__(self, name="", typing="Static", reflection=False, year=0):
        """Initialise programming languages instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return str(self)

    def is_dynamic(self):
        """Determine if programming language is dynamic"""
        return self.typing == "Dynamic"
