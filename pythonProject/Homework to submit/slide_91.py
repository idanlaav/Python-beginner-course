# Exercise 1
print("Start exercise 1 ---------------------------------------------------- Start exercise 1")

import os
from pathlib import Path
def create_file_on_desktop(file_name):
    # Get the user's home directory
    home_dir = Path.home()
    # Check the operating system and set the desktop path accordingly
    if os.name == 'posix' or os.name == 'nt':  # Mac or Linux or Windows
        desktop_path = home_dir / 'Desktop'
    else:
        raise OSError("Unsupported operating system")
    # Create the file on the desktop
    file_path = desktop_path / file_name
    # Check if the file already exists
    if file_path.exists():
        print(f"The file '{file_name}' already exists on the desktop.")
    else:
        # Create the file
        with open(file_path, 'w') as file:
            # I am using in the function at exercise 3 so i do not want to insert that content inside to the other file
            if file_name == 'myFile.txt':
                file.write("Python is great")
        print(f"The file '{file_name}' has been created on the desktop.")
# Specify the file name
file_name = 'myFile.txt'
# Call the function to create the file
create_file_on_desktop(file_name)

print("End exercise 1 ------------------------------------------------------ End exercise 1\n")


# Exercise 2
print("Start exercise 2 ---------------------------------------------------- Start exercise 2")

# There is an import of pathlib in exercise 1
file_path = Path.home() / 'Desktop' / file_name
# Read existing content before opening the file in append mode
with open(file_path, 'r') as f:
    existing_content = f.read().splitlines()
# Create or open the file in append mode
with open(file_path, 'a+') as f:
    list_of_names = ['Idan Laav', 'Omer Laav', 'Agam Laav', 'Eran Laav', 'Iris Laav']
    for person in list_of_names:
        # Check if the name is already in the file
        if person not in existing_content:
            f.write("\n")
            f.write(person)
            print(f"Added {person} to the file.")
            existing_content.append(person)  # Update existing content
        else:
            print(f"{person} is already in the file.")
print("The names have been successfully processed.")

print("End exercise 2 ------------------------------------------------------ End exercise 2\n")


# Exercise 3
print("Start exercise 3 ---------------------------------------------------- Start exercise 3")

another_file_name = "myFile2.txt"
# Using function from exercise 1
create_file_on_desktop(another_file_name)
file_path_2 = Path.home() / 'Desktop' / another_file_name
myFile = open(file_path, 'r')
content = myFile.read()
with open(file_path_2, 'w') as file:
    file.write(content)

print("End exercise 3 ------------------------------------------------------ End exercise 3\n")


# Exercise 4
print("Start exercise 4 ---------------------------------------------------- Start exercise 4")

with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)
    print(f"myFile has {line_count} lines.")

with open(file_path_2, 'r') as file:
    line_count = sum(1 for line in file)
    print(f"myFile has {line_count} lines.")

print("End exercise 4 ------------------------------------------------------ End exercise 4\n")