"""
Wimbledon
"""
import csv

FILENAME = "wimbledon.csv"


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        data = list(reader)
    countries = set([row[1] for row in data])
    champions = [row[2] for row in data]
    champion_to_count = {champion: champions.count(champion) for champion in champions}
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
