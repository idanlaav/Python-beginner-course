# Exercise 1
import os
first_text_file = open('first_text_file.txt', 'w')
second_text_file = open('second_text_file.txt', 'w')
first_names = ['Idan','Omer','Agam','Iris','Eran']
last_name = 'Laav'
for name in first_names:
    first_text_file.write(f"{name}\n")
second_text_file.write(last_name)
first_text_file.close()
second_text_file.close()

first_text_file = open('first_text_file.txt', 'r')
second_text_file = open('second_text_file.txt', 'r')
first_file_data = first_text_file.read().strip()
second_file_data = second_text_file.read().strip()
# I opened that file outside of this directory because, in Exercise 2, it will be deleted.
marge_text_files = open('../marge_text_files.txt', 'w')
for name in first_file_data.split('\n'):
    marge_text_files.write(f"{name} {second_file_data}\n")

first_text_file.close()
second_text_file.close()
os.remove('first_text_file.txt')
os.remove('second_text_file.txt')
marge_text_files.close()

print("Files merged and original files removed.")