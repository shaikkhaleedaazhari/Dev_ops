import os
directory = input("enter your dir:")
if os.path.exists(directory) and os.path.isdir(directory):
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)    
            print(f"{file}: {file_size} bytes")
else:
    print("The specified directory does not exist.")

# import os

# directory = input("Enter your directory: ")

# if os.path.exists(directory) and os.path.isdir(directory):
#     print(f"Directory '{directory}' exists!")  # Debugging print
#     files = os.listdir(directory)
    
#     if not files:
#         print("The directory is empty.")  # Debugging print
    
#     for file in files:
#         file_path = os.path.join(directory, file)
#         if os.path.isfile(file_path):
#             file_size = os.path.getsize(file_path)
#             print(f"{file}: {file_size} bytes")
#         else:
#             print(f"Skipping directory: {file}")  # Debugging print
# else:
#     print("The specified directory does not exist.")



