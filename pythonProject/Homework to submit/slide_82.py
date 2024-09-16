# Exercise 1
import math
print(math.pi)

# Exercise 2
import sys
print(sys.version)

# Exercise 3
import os
print(os.getcwd())

# Exercise 4
# There is an import of os in exercise 3
new_directory_name = "this_is_the_new_directory_that_created_by_function_mkdir_in_module_os"
current_directory_list = os.listdir(os.getcwd())
if new_directory_name not in current_directory_list:
    os.mkdir(new_directory_name)


# Exercise 5
import random
x = random.randrange(1,100)
number_of_tries = 0
while True:
    user_guess = int(input("Guess the number (between 1-100): "))
    number_of_tries += 1
    if x < user_guess:
        print("Too high, please try again.")
    elif x > user_guess:
        print("Too low, please try again.")
    else:
        if number_of_tries == 1:
            print(f"Congratulation you did in {number_of_tries} try!")
        else:
            print(f"Congratulation you did in {number_of_tries} tries!")
        break
    if number_of_tries == 5:
        print("Game over, better luck next time.")
        break
