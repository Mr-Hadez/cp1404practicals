"""
CP1404/CP5632 Practical
Wikipedia API
"""

import wikipedia


def main():
    """Prompts user for page title and print some details of the page, ends when user enters blank input."""
    title = input("Enter page title: ")
    while title != "":
        print_page_details(title)
        title = input("Enter page title: ")
    print("Thank you.")


def print_page_details(title):
    """Print page title, short summary and URL."""
    page = wikipedia.page(title)
    print(page.title)
    print(wikipedia.summary(title, 4))  # Truncate output to match sample output
    print(page.url)


if __name__ == '__main__':
    main()
