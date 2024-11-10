"""
Project Management program
Estimate: 45 minutes
Actual:   50 minutes
"""

from operator import attrgetter
import datetime

from prac_03.capitalist_conrad import FILENAME
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
            filename = input("Filename: ")
            save_data(filename, projects)
        elif choice == "D":
            display_project_details(projects)
        elif choice == "F":
            filtered_projects = filter_projects(projects)
            filtered_projects.sort(key=attrgetter("start_date"))
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
    save_prompt = input(f"Would you like to save to {DEFAULT_FILE}? ").upper()
    if save_prompt == "YES" or save_prompt == "Y":
        save_data(projects, DEFAULT_FILE)
    print("Thank you for using custom-built project management software.")


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


def filter_projects(projects):
    filter_date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.is_after_date(filter_date)]
    return filtered_projects


def update_project(project):
    completion_percentage = get_valid_int("New Percentage: ", min_value=0, max_value=100)
    priority = get_valid_int("Priority: ", min_value=1)
    project.priority = priority
    project.completion_percentage = completion_percentage


def get_valid_int(prompt, min_value=None, max_value=None):
    """Prompt the user for an integer and validate the input."""
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input; please enter a valid integer.")


def get_valid_float(prompt, min_value=None, max_value=None):
    """Prompt the user for a float and validate the input."""
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input; please enter a valid number.")


def get_valid_date(prompt):
    """Prompt the user for a date and validate the format."""
    while True:
        date_string = input(prompt)
        try:
            return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format; please enter date as dd/mm/yyyy.")


def get_non_empty_string(prompt):
    """Prompt the user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be blank. Please enter a valid value.")


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
    name = get_non_empty_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_int("Priority: ", min_value=1)  # Assuming priority should be a positive integer
    cost_estimate = get_valid_float("Cost estimate: $", min_value=0)  # Assuming cost should be non-negative
    completion_percentage = get_valid_int("Completion percentage: ", min_value=0, max_value=100)
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def save_data(projects, filename):
    """Save projects to file."""
    with open(filename, "w", newline="") as out_file:
        for project in projects:
            line = f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.completion_percentage}\n"
            out_file.write(line)


if __name__ == '__main__':
    main()
