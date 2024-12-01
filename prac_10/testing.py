"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    words = []
    for i in range(n):
        words.append(s)
    return " ".join(words)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly"
    car = Car()
    assert car.fuel == 0, "Car does not set fuel correctly"


def format_phrase(string):
    """
       Format phrase as a sentence
       >>> format_phrase("hello")
       'Hello.'
       >>> format_phrase("It is an ex parrot.")
       'It is an ex parrot.'
       >>> format_phrase("python.")
       'Python.'
       """
    string = list(string)
    string[0] = string[0].upper()
    if string[-1] != ".":
        string.append(".")
    return "".join(string)


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()
