# def sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(sum(5,6,7))
#
# def avg(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum / len(args)
# print(avg(5,6,7))

# def avg(*args):
#     return sum(args) / len(args)
# print(avg(5,6,7))






# print()
# input()
# sum()
# len()
# type()
# map()
# lambda
# list()
# set()
# int()
# tuple()
# replace()
# range()
# upper()


# list1 = [1,2,3,4]
# list1 = set(list1)
# print(list1)


# x = {4,5,6}
# print(type(x))

# insert two parm the first is function and the second is iterable getting the function power and run it on the l1
# l1 = [1,2,3,4,5,6]
# def power(x):
#     return x**2
# print(list(map(power, l1)))
#
#
# def add_underline(s):
#     return s + '_'
# for i in map(add_underline,"hello"):
#     print(i, end='')

# lambda unanimous function that we used in one place
# for i in map(lambda s:s + '_' ,"hello"):
#     print(i, end='')

# l1 = [1,2,3,4,5,6]
# print(list(map(lambda x: x**2, l1)))


# l1 = [1,2,3,4,5,6]
# l1 = (list(map(lambda x:x**2, l1)))
# print(list(filter(lambda x:x%2==0,l1)))



# help() # will show the  information about the function
# import math
# help(math)


# import sys
# print(sys.version)
# print('\n'.join(sys.path))


# import sys
# sys.path.append(r'/Users/laav/Documents/Python/01') # place of the file that we build
# import hello


# we download module requests from pypi.org
# import requests
# response = requests.get("http://www.google.co.il")
# print(response.text)


# import os
# print(os.listdir(r'/Users/laav/Documents/Python/01')) # show all the files in this position
# os.mkdir() # make a folder
# os.remove() # remove a folder
# print(os.getcwd()) # current folder


# f = open(r'/Users/laav/Documents/Python/01/hello.py')
# print(f.read())

# f = open(r'a.txt')
# print(f.read())
# print(''.join(f.read/lines()[2:]))


# f = open(r'a.txt', 'r') # only for read

# f = open(r'b.txt', 'w') # make new file and adding
# print(f.write('hello\nworld'))

# f = open(r'b.txt', 'a') # adding to the file and not clear him # if we will use a+ or w+ it the first one + reading
# f.write('hello\nworld\nidan\nlaav')
# f.write('\nit is working')

# import os
# def merge_text_files(folder):
#     for filename in os.listdir(folder):
#         if filename.endswith('.txt'):
#             print(filename)
# merge_text_files(os.getcwd())

# import os
# def merge_text_files(folder):
#     merged_text = ''
#     for i in [filename for filename in os.listdir() if filename.endswith('.txt')]:
#         # print(open(i).read())
#         merged_text += open(i).read()
#         merged_text += "\n"
#         open('./marge/merged_file.txt', 'w').write(merged_text)
# merge_text_files(os.getcwd())




# f = open(r'/Users/laav/Documents/Python/student_table.csv')
# print(f.read())
# print(f.readlines()[1:])

# for row in f.readlines()[1:]:
#     print(int(row.split(',')[1]))

# import csv
# f = open(r'/Users/laav/Documents/Python/student_table.csv')
# reader = csv.DictReader(f)
# for row in reader:
#     print(row['age'])


# import csv
# from math_1 import avg
# f = open(r'/Users/laav/Documents/Python/student_table.csv')
# reader = csv.DictReader(f)
# print([int(row['age']) for row in reader])
# print(avg([int(row['age']) for row in reader]))


# import csv
# f = open(r'/Users/laav/Documents/Python/student_table.csv')
# reader = csv.DictReader(f)
# print(list(reader))


# import csv
# f = open(r'/Users/laav/Documents/Python/student_table.csv', 'a+')
# f.seek() # will put the new items in some position we choose
# reader = csv.DictReader(f)
# print(list(reader))



# import requests
# response = requests.get('https://randomuser.me/api')
# dict1 = response.json()
# print(dict1)


# import requests
# response = requests.get('https://randomuser.me/api')
# dict1 = response.json()
# print(dict1['results'][0]['name'])
# row = {}
# row["firstname"] = dict1['results'][0]['name']['first']
# row["lastname"] = dict1['results'][0]['name']['first']
# row["country"] = dict1['results'][0]['location']['country']
# row["email"] = dict1['results'][0]['email']
# import csv
# f = open('users.csv', 'a+', encoding='utf-8', newline='')
# writer = csv.DictWriter(f, fieldnames=['firstname','lastname','country','email'])
# # writer.writeheader()
# writer.writerow(row)