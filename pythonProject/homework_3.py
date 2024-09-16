# Slide 77
# Exercise 1
# original_list = [12,-1,9,8,-0.5,-0.2,-100]
# negative_numbers = sorted(filter(lambda x: x < 0, original_list))
# print(f"Answer to exercise 1: {negative_numbers}")

# Exercise 2
# original_list = [12,-1,9,8,-0.5,-0.2,-100]
# even_numbers = sorted(filter(lambda x: x % 2 == 0, original_list))
# print(f"Answer to exercise 2: {even_numbers}")

# Exercise 3
# original_list_number_2 = [1000,500,600,700,5000,90000,17500]
# result = sorted(list(map(lambda x: x + 2000, filter(lambda x: x < 8000, original_list_number_2))))
# print(f"Answer to exercise 3: {result}")

# Exercise 4
# original_list_number_3 = [-1000,500,-600,700,5000,-90000,-17500]
# converted_numbers = sorted(list(map(lambda x: x*-1, filter(lambda x: x < 0, original_list_number_3))))
# print(f"Answer to exercise 4: {converted_numbers}")


# Slide 80
# Exercise 1
# def kg_to_lbs(kg):
#     return kg * 2.2046
#
# def lbs_to_kg(lbs):
#     return lbs / 2.2046

# Exercise 2
# kg_100 = 100
# print(f"100 kilogram is equal to: {kg_to_lbs(kg_100)} lbs.")

# Exercise 3
# def inch_to_centimeter(inch):
#     return inch * 2.54
#
# def centimeter_to_inch(cm):
#     return cm / 2.2046

# Exercise 4
# inch_50 = 50
# print(f"50 inch is equal to: {inch_to_centimeter(inch_50)} centimeter.")


# Slide 82
# Exercise 1
# import math
# print(math.pi)

# Exercise 2
# import sys
# print(sys.version)

# Exercise 3
# import os
# print(os.getcwd())

# Exercise 4
# import os
# new_directory_name = "this_is_the_new_directory_that_created_by_function_mkdir_in_module_os"
# current_directory_list = os.listdir(os.getcwd())
# if new_directory_name not in current_directory_list:
#     os.mkdir(new_directory_name)


# Exercise 5
# import random
# x = random.randrange(1,100)
# number_of_tries = 0
# while True:
#     user_guess = int(input("Guess the number (between 1-100): "))
#     number_of_tries += 1
#     if x < user_guess:
#         print("Too high, please try again.")
#     elif x > user_guess:
#         print("Too low, please try again.")
#     else:
#         if number_of_tries == 1:
#             print(f"Congratulation you did in {number_of_tries} try!")
#         else:
#             print(f"Congratulation you did in {number_of_tries} tries!")
#         break
#     if number_of_tries == 5:
#         print("Game over, better luck next time.")
#         break


# Slide 91
# print("Start exercise 1 ---------------------------------------------------- Start exercise 1")
#
# import os
# from pathlib import Path
# def create_file_on_desktop(file_name):
#     # Get the user's home directory
#     home_dir = Path.home()
#     # Check the operating system and set the desktop path accordingly
#     if os.name == 'posix':  # Mac or Linux
#         desktop_path = home_dir / 'Desktop'
#     elif os.name == 'nt':  # Windows
#         desktop_path = home_dir / 'Desktop'
#     else:
#         raise OSError("Unsupported operating system")
#     # Create the file on the desktop
#     file_path = desktop_path / file_name
#     # Check if the file already exists
#     if file_path.exists():
#         print(f"The file '{file_name}' already exists on the desktop.")
#     else:
#         # Create the file
#         with open(file_path, 'w') as file:
#             # I am using in the function at exercise 3 so i do not want to insert that content inside to the other file
#             if file_name == 'myFile.txt':
#                 file.write("Python is great")
#         print(f"The file '{file_name}' has been created on the desktop.")
# # Specify the file name
# file_name = 'myFile.txt'
# # Call the function to create the file
# create_file_on_desktop(file_name)
#
# print("End exercise 1 ------------------------------------------------------ End exercise 1\n")
#
#
# # Exercise 2
# print("Start exercise 2 ---------------------------------------------------- Start exercise 2")
#
# # There is an import of pathlib in exercise 1
# file_path = Path.home() / 'Desktop' / file_name
# # Read existing content before opening the file in append mode
# with open(file_path, 'r') as f:
#     existing_content = f.read().splitlines()
# # Create or open the file in append mode
# with open(file_path, 'a+') as f:
#     list_of_names = ['Idan Laav', 'Omer Laav', 'Agam Laav', 'Eran Laav', 'Iris Laav']
#     for person in list_of_names:
#         # Check if the name is already in the file
#         if person not in existing_content:
#             f.write("\n")
#             f.write(person)
#             print(f"Added {person} to the file.")
#             existing_content.append(person)  # Update existing content
#         else:
#             print(f"{person} is already in the file.")
# print("The names have been successfully processed.")
#
# print("End exercise 2 ------------------------------------------------------ End exercise 2\n")
#
#
# # Exercise 3
# print("Start exercise 3 ---------------------------------------------------- Start exercise 3")
#
# another_file_name = "myFile2.txt"
# # Using function from exercise 1
# create_file_on_desktop(another_file_name)
# file_path_2 = Path.home() / 'Desktop' / another_file_name
# myFile = open(file_path, 'r')
# content = myFile.read()
# with open(file_path_2, 'w') as file:
#     file.write(content)
#
# print("End exercise 3 ------------------------------------------------------ End exercise 3\n")
#
#
# # Exercise 4
# print("Start exercise 4 ---------------------------------------------------- Start exercise 4")
#
# with open(file_path, 'r') as file:
#     line_count = sum(1 for line in file)
#     print(f"myFile has {line_count} lines.")
#
# with open(file_path_2, 'r') as file:
#     line_count = sum(1 for line in file)
#     print(f"myFile has {line_count} lines.")
#
# print("End exercise 4 ------------------------------------------------------ End exercise 4\n")


# Slide 98
# Exercise 1
# import csv
# import random
# file_name = 'dice.csv'
# new_file = open(file_name, 'w')
# column_names = ['dice1','dice2']
# writer = csv.writer(new_file)
# writer.writerow(['dice1', 'dice2'])
# for i in range(1,21):
#     writer.writerow([random.randrange(1,6), random.randrange(1,6)])
# new_file.close()


# # Exercise 2
# import csv
# new_file = open(file_name, 'r')
# reader = csv.DictReader(new_file)
# columns_numbers_value = [int(row['dice1']) + int(row['dice2']) for row in reader]
# avg = sum(columns_numbers_value) / len(columns_numbers_value)
#
# print("Numbers in 'dice1' column:", columns_numbers_value)
# print("The avg of the numbers that exist in column 'dice1' is:", avg)


# Slide 104
# Exercise 1
# import os
# first_text_file = open('first_text_file.txt', 'w')
# second_text_file = open('second_text_file.txt', 'w')
# first_names = ['Idan','Omer','Agam','Iris','Eran']
# last_name = 'Laav'
# for name in first_names:
#     first_text_file.write(f"{name}\n")
# second_text_file.write(last_name)
# first_text_file.close()
# second_text_file.close()
#
# first_text_file = open('first_text_file.txt', 'r')
# second_text_file = open('second_text_file.txt', 'r')
# first_file_data = first_text_file.read().strip()
# second_file_data = second_text_file.read().strip()
# marge_text_files = open('marge_text_files.txt', 'w')
# for name in first_file_data.split('\n'):
#     marge_text_files.write(f"{name} {second_file_data}\n")
#
# first_text_file.close()
# second_text_file.close()
# os.remove('first_text_file.txt')
# os.remove('second_text_file.txt')
# marge_text_files.close()
#
# print("Files merged and original files removed.")


# Slide 117
# Exercise 1
# import csv
# import requests
#
# file_name = 'coin_base_data.csv'
# r = requests.get('https://api.coinbase.com/v2/currencies')
# data = r.json()['data']
#
# # Collect unique keys in a set
# unique_keys = set()
# for item in data:
#     unique_keys.update(item.keys())
#
# column_names = list(unique_keys)
#
# new_file = open(file_name, 'w')
# writer = csv.writer(new_file)
# writer.writerow(column_names)
#
# for coin in data:
#     row_data = [coin.get(column, '') for column in column_names]
#     writer.writerow(row_data)
#
# new_file.close()


# Slide 117
# Exercise 1
# import csv
# import requests
#
# file_name = 'coin_base_data.csv'
# r = requests.get('https://api.coinbase.com/v2/currencies')
# dict1 = r.json()['data']
#
# f = open('coinbase.csv', 'a', encoding='utf-8', newline='')
# writer = csv.DictWriter(f, fieldnames=['id', 'name', 'min_size'])
# writer.writeheader()
# writer.writerow(dict1)


