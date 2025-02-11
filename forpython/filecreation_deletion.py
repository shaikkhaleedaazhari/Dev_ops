# import os
# import time
# def create_files(directory, file_names):
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     for file_name in file_names:
#         file_path = os.path.join(directory, file_name)
#         with open(file_path, 'w') as file:
#             file.write("This is a sample file: " + file_name)
#         print(f"Created: {file_path}")

# def delete_files(directory, file_names, delay):
#     time.sleep(delay)
#     for file_name in file_names:
#         file_path = os.path.join(directory, file_name)
#         if os.path.exists(file_path):
#             os.remove(file_path)
#             print(f"Deleted: {file_path}")
#         else:
#             print(f"File not found: {file_path}")

# directory = input("Enter Directory Path")
# file_names = list(map(str,input("Enter file names to create and delete").split(" ")))
# delay = 10  
# create_files(directory, file_names)
# delete_files(directory, file_names, delay)
























import os

def create_file(directory, filename, content):
    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    
    # Create the file with the specified content
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(content)
    print(f"File '{filename}' created with your content.")

def delete_file(directory, filename):
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")

# Ask for user input
directory = input("Enter the directory: ")
action = input("Do you want to create or delete a file? (create/delete): ").strip().lower()
filename = input("Enter the filename: ").strip()

# Perform the requested action
if action == "create":
    content = input("Enter the content for the file: ")
    create_file(directory, filename, content)
elif action == "delete":
    delete_file(directory, filename)
else:
    print("Invalid action.")