# Exercise 3
import os
from pathlib import Path
def create_folder(name):
    full_path = Path(os.getcwd()) / name
    if full_path.exists():
        print(f"This folder '{name}' already exists in this path.")
    else:
        os.mkdir(name)
        print(f"The folder: '{name}', was successfully added.")

folder_name = 'my_folder'
create_folder(folder_name)


current_path = Path(os.getcwd()) / folder_name / 'desktop.txt'
def get_files_only(directory):
    file_names = [
        item
        for item in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, item))
           and not os.path.islink(os.path.join(directory, item))
           and not item.startswith('.')
           and '.' in item
    ]
    return file_names

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
files_on_desktop = get_files_only(desktop_path)

with open(current_path, 'w') as new_file:
    for name in files_on_desktop:
        new_file.write(name + "\n")

print(f"File 'desktop.txt' created at {current_path}")
