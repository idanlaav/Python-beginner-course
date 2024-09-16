# שקופית 46 תרגיל 1
# for i in range(10, 101, 10):
# print(i)
# print(i, end=",") # end="" what you put inside the "" is the symbol that will display instead \n that is the default settings

# שקופית 46 תרגיל 2
# for i in range(5, 0, -1):
#     print(i,end=',')
# print("boom")

# שקופית 46 תרגיל 3
# for a in range(1, 11):
#     for b in range(1, 11):
#         print(a*b,end="\t") # \t = tab
#     print()

# שקופית 46 תרגיל 4
# for a in range(5):
#     for b in range(5-a , 0 , -1):
#         print(b, end=" ")
#     print()



# שקופית 50 תרגיל 1
# for i in range(100):
#     print(i)
#     if i == 7:
#         break
# print("End loop.")

# שקופית 50 תרגיל 2
# weather = ["snow","rain","sun","clouds"]
# for i in weather:
#     if i == "sun":
#         continue
#     print(i)
# print("End loop.")

# שקופית 50 תרגיל 3
# for i in range(2,8):
#     if i % 2 == 0:
#         print(f"Found a even number {i}")
#     else:
#         print(f"Found a number {i}")



# שקופית 51 תרגיל 1
# for num in range(4, 11):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} is a primary number.")
#     else:
#         print(f"{num} is not a primary number.")



# שקופית 53 תרגיל 1
# x = 47
# number_of_tries = 0
# correct = False
# while correct != True:
#     user_guess = int(input("Guess the number (between 1-100: "))
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



# שקופית 54 תרגיל 1
# my_list1 = [1,2,3,4,5,6,7,8,9]
# del my_list1[1]
# print(my_list1)

# שקופית 54 תרגיל 2
# my_list1 = [1,2,3,4,5,6,7,8,9]
# del my_list1[3:6]
# print(my_list1)

# שקופית 54 תרגיל 3
# my_list1 = [1,2,3,4,5,6,7,8,9]
# del my_list1
# print(my_list1)



# שקופית 58 תרגיל 1
# test = {0:10,1:20}
# test[2] = 30
# print(test)

# שקופית 58 תרגיל 2
# inventory = {"shirts":25,"paints":220,"shocks":525,"tshirts":217}
# print(inventory)
# inventory.pop("tshirts")
# print(f"Removed ('tshirts', {inventory.pop('tshirts')})")
# print(inventory)



# שקופית 60 תרגיל 1
# fruits = ("apple","banana","cherry")
# print(fruits[1])

# שקופית 60 תרגיל 2
# first_tuple = (11,22,33,44,55,66)
# new_tuple = first_tuple[4:]
# print(new_tuple)


# שקופית 60 תרגיל 3
# first_tuple = (11,[22,33],44,55,66)
# first_tuple = list(first_tuple)
# first_tuple[1][0] = 222
# first_tuple = tuple(first_tuple)
# print(first_tuple)
# # Modify the nested list element
# first_tuple = first_tuple[:1] + ([222] + first_tuple[1][1:],) + first_tuple[2:]
# print(first_tuple)



# שקופית 64 תרגיל 1
# list1 = ["green","blue"]
# list2 = ["blue","yellow"]
# result = set(list1) ^ set(list2)
# print(result)



# שקופית 70 תרגיל 1
# def palindrome_check(value):
#     if value == value[::-1]:
#         print("yes")
#     else:
#         print("no")
#
# user_value = input("Enter a value: ")
# palindrome_check(user_value)
