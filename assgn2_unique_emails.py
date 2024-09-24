import re

def extract_unique_emails(file_path):

    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    unique_emails = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:

                emails = email_pattern.findall(line)

                unique_emails.update(emails)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return [], 0


    sorted_emails = sorted(unique_emails)
    return sorted_emails, len(sorted_emails)

# Example usage
if __name__ == "__main__":
    file_path = 'unique emails.txt'
    emails, count = extract_unique_emails(file_path)
    print(f"Unique email addresses ({count}):")
    for email in emails:
        print(email)
