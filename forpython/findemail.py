#Implement a regular expression to search for email addresses in a text file.

import re

file_path = input("Enter the file path: ")

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

try:
    with open(file_path, 'r') as f:
        file_content = f.read()
    
    emails = re.findall(email_pattern, file_content)

    if emails:
        print("\nEmail addresses found in the file:")
        for email in emails:
            print(email)
    else:
        print("\nNo email addresses found.")

except FileNotFoundError:
    print("\nError: The specified file does not exist.")
except Exception as e:
    print(f"\nAn error occurred: {e}")

