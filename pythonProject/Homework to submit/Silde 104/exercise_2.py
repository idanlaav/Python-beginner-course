# Exercise 2
import os
first_text_file = open('first_text_file.txt', 'w+')
first_text_file.write('Hello,')
second_text_file = open('second_text_file.txt', 'w+')
second_text_file.write('my name is idan.')
third_text_file = open('third_text_file.txt', 'w+')
third_text_file.write('I am 24 years old.')
fourth_text_file = open('fourth_text_file.txt', 'w+')
fourth_text_file.write('I am living in Petah Tikva.')
fifth_text_file = open('fifth_text_file.txt', 'w+')
fifth_text_file.write('Good bye')

# Move the file pointers to the beginning
first_text_file.seek(0)
second_text_file.seek(0)
third_text_file.seek(0)
fourth_text_file.seek(0)
fifth_text_file.seek(0)

# Collect data from .txt files only
merge_data = ''
for file_name in os.listdir():
    if file_name.endswith('.txt'):
        current_file_path = os.path.join(os.getcwd(), file_name)
        current_file = open(current_file_path, 'r')
        merge_data += current_file.read() + '\n'
        current_file.close()
        os.remove(current_file_path)

new_file = open('merge_file.txt', 'w')
new_file.write(merge_data)
new_file.close()
