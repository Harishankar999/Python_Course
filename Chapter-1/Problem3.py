import os

# Specify the you want to list 
directory_path = "/Python_Course"

# List all files and directories in the specific path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item);