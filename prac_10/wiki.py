"""
CP1404/CP5632 Practical
Wikipedia API
"""

import wikipedia


def main():
    """Prompts user for page title and print some details of the page, ends when user enters blank input."""
    title = input("Enter page title: ")
    while title != "":
        display_page_details(title)
        title = input("Enter page title: ")
    print("Thank you.")


def display_page_details(title):
    """Print page title, short summary and URL."""
    try:
        page = wikipedia.page(title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.suggest(title))
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    else:
        print(page.title)
        print(page.summary)
        print(page.url)


if __name__ == '__main__':
    main()
