# Exercise 1
import csv
import random
file_name = 'dice.csv'
new_file = open(file_name, 'w')
column_names = ['dice1','dice2']
writer = csv.writer(new_file)
writer.writerow(['dice1', 'dice2'])
for i in range(1,21):
    writer.writerow([random.randrange(1,6), random.randrange(1,6)])
new_file.close()



# Exercise 2
# Using in the import of csv from exercise 1
new_file = open(file_name, 'r')
reader = csv.DictReader(new_file)
columns_numbers_value = [int(row['dice1']) + int(row['dice2']) for row in reader]
avg = sum(columns_numbers_value) / len(columns_numbers_value)

print("Numbers in 'dice1' column:", columns_numbers_value)
print("The avg of the numbers that exist in column 'dice1' is:", avg)