"""
Email
Estimate: 20 minutes
Actual:   40 minutes
"""


def main():
    """Get email and extract name and store in dictionary."""
    email_to_name = {}
    email = input('Email: ')
    while email != "":
        name = extract_name(email)
        choice = input(f'Is your name {name} (Y/n) ').upper()
        if choice != 'Y' and choice != '':
            name = input('Name: ')
        email_to_name[email] = name
        email = input('Email: ')
    for email, name in sorted(email_to_name.items()):
        print(f"{name} ({email})")


def extract_name(email):
    """Split first part of email to extract full name."""
    parts = (email.split('@')[0]).split('.')
    name = " ".join(parts).title()
    return name


main()
