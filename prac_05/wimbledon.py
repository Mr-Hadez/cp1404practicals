"""
Wimbledon
"""
import csv

FILENAME = "wimbledon.csv"


def main():
    """Get data, extract champion information and display data."""
    data = get_data()
    champion_to_count, countries = extract_data(data)
    display_data(champion_to_count, countries)


def get_data():
    """Read wimbledon file and return data."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        data = list(reader)
    return data


def extract_data(data):
    """Extract countries in a set and champions and count to a dictionary."""
    countries = {row[1] for row in data}
    champion_to_count = {}
    for row in data:
        try:
            champion_to_count[row[2]] += 1
        except KeyError:
            champion_to_count[row[2]] = 1
    return champion_to_count, countries


def display_data(champion_to_count, countries):
    """Print champions and number of times they have won and all the champion countries."""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
