import csv


def gather_user_input():
    user_input = input('Enter file relative or absolute path: ')
    return user_input


def remove_dups_from_email_list(emails):
    important_emails = list({email for email in emails if emails.count(email) > 1})
    for email in important_emails:
        print(email)


def read_csv_compose_email_list():
    while True:
        try:
            user_input = gather_user_input()
            with open(user_input, mode='r') as f:
                reader = csv.reader(f)
                next(reader)
                emails = [email[10] for email in reader if email[10] != '']
                return emails
        except FileNotFoundError:
            print("\nFile not found...")
            input("Press ENTER to try again...")


def main():
    emails = read_csv_compose_email_list()
    remove_dups_from_email_list(emails)


if __name__ == '__main__':
    main()
