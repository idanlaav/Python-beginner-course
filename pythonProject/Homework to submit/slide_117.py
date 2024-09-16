# Exercise 1
import csv
import requests

file_name = 'coin_base_data.csv'
r = requests.get('https://api.coinbase.com/v2/currencies')
data = r.json()['data']

# Collect unique keys in a set
unique_keys = set()
for item in data:
    unique_keys.update(item.keys())

column_names = list(unique_keys)

new_file = open(file_name, 'w')
writer = csv.writer(new_file)
writer.writerow(column_names)

for coin in data:
    row_data = [coin.get(column, '') for column in column_names]
    writer.writerow(row_data)

new_file.close()

