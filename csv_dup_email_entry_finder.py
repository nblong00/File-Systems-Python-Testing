import csv


def gather_user_input():
    user_input = input('Enter file relative or absolute path: ')
    return user_input


def remove_dups_from_email_list(emails):
    important_emails = list({email for email in emails if emails.count(email) > 1})
    print(important_emails)


def read_csv_compose_email_list(user_input):
    with open(user_input, mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        emails = [email[10] for email in reader if email[10] != '']
        return emails


def main():
    user_input = gather_user_input()
    emails = read_csv_compose_email_list(user_input)
    remove_dups_from_email_list(emails)


if __name__ == '__main__':
    main()
