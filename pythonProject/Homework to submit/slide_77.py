# Exercise 1
original_list = [12,-1,9,8,-0.5,-0.2,-100]
negative_numbers = sorted(filter(lambda x: x < 0, original_list))
print(f"Answer to exercise 1: {negative_numbers}")

# Exercise 2
# The original list is exist in exercise 1
even_numbers = sorted(filter(lambda x: x % 2 == 0, original_list))
print(f"Answer to exercise 2: {even_numbers}")

# Exercise 3
original_list_number_2 = [1000,500,600,700,5000,90000,17500]
result = sorted(list(map(lambda x: x + 2000, filter(lambda x: x < 8000, original_list_number_2))))
print(f"Answer to exercise 3: {result}")

# Exercise 4
original_list_number_3 = [-1000,500,-600,700,5000,-90000,-17500]
converted_numbers = sorted(list(map(lambda x: x*-1, filter(lambda x: x < 0, original_list_number_3))))
print(f"Answer to exercise 4: {converted_numbers}")