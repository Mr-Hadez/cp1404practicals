"""
Project Management program
Estimate: 45 minutes
Actual:   50 minutes
"""

from operator import attrgetter
import datetime
from project import Project

DEFAULT_FILE = "projects.txt"
MENU_STRING = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\nQ-Quit"


def main():
    """Load menu for user to choose to load, save and display projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_data(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    choice = load_menu()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_data(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            display_project_details(projects)
        elif choice == "F":
            filter_date_string = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
            filtered_projects = [project for project in projects if project.is_after_date(filter_date)]
            for project in filtered_projects:
                print(project)
        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(i, project)
            project = choose_project(projects)
            update_project(project)
        else:
            print("Invalid menu choice")
        choice = load_menu()
    save_data(projects)
    print(f"{len(projects)} places saved to {DEFAULT_FILE}")
    print("Have a nice day :)")


def load_data(filename):
    """Load file and convert it into a list of lists."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def load_menu():
    """Load menu for user input."""
    print(MENU_STRING)
    choice = input(">>> ").upper()
    return choice


def display_project_details(projects):
    """Display project details in a neat format."""
    print("Incomplete projects: ")
    projects.sort(key=attrgetter("priority"))
    incomplete_projects = [project for project in projects if project.is_complete() is False]
    for project in incomplete_projects:
        print(project)
    print("Complete projects: ")
    complete_projects = [project for project in projects if project.is_complete()]
    for project in complete_projects:
        print(project)


def update_project(project):
    completion_percentage = int(input("New Percentage: "))
    priority = int(input("Priority: "))
    project.priority = priority
    project.completion_percentage = completion_percentage


def get_valid_input():
    """Get valid user input for name and country."""
    name = input("Name: ")
    while not name:
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Input can not be blank")
        country = input("Country: ")
    return country, name


def choose_project(projects):
    """Get place to mark as visited."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("Project choice: "))
            if number < 0:
                print("Number must be >= 0")
            elif number > len(projects):
                print("Invalid place number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    project = projects[number]
    print(project)
    return project


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Completion percentage: "))
    project = Project(name, date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def save_data(places):
    """Save data list to places.csv file."""
    with open(FILENAME, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerows(places)


if __name__ == '__main__':
    main()
