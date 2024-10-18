"""
Email
Estimate: 20 minutes
Actual:   40 minutes
"""
def main():
    email_to_name = {}
    email = input('Email: ')
    while email != "":
        first_name = (email.split('@')[0]).split('.')[0]
        if '.' in email.split('@')[0]:
            last_name = (email.split('@')[0]).split('.')[1]
        else:
            last_name = ''
        email_to_name[email] = f"{first_name} {last_name}"
        choice = input(f'Is your name {email_to_name[email]} (Y/n) ').upper()
        if choice == 'Y':
            email = input('Enter your email: ')
        else:
            name = input('Name: ')
            email_to_name[email] = name
            email = input('Enter your email: ')
    for email, name in sorted(email_to_name.items()):
        print(f"{name} ({email})")

main()
