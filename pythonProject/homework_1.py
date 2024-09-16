# תרגיל 1 שקופית 13
# pi = 3.14159
# radius = 12
# sum = pi*radius*2
# print(pi*radius**2)


# תרגיל 1 שקופית 18
# firstname = input("Enter you first name: ")
# lastname = input("Enter you last name: ")
# print(f"""{firstname.capitalize()}
# {lastname.capitalize()}""")

# תרגיל 2 שקופית 18
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# result = f"{firstname.capitalize()} {lastname.capitalize()} | " * 5
# print(result[:-2])  # This removes the last two characters, which are the space and the |

# תרגיל 3 שקופית 18
# print("""Twinkle,twinkle,little star,
#               How I wonder what you are!
#                    Up above the world so high,
#                    Like a diamond in the sky.""")


# תרגיל 1 שקופית 22
# text = "Hello world"
# print(text[4])

# תרגיל 2 שקופית 22
# text = "Hello world"
# print(text[-2])

# תרגיל 3 שקופית 22
# text = "Hello world"
# print(text[6:])
# print(text.split()[1])
# index = text.find(" ")  # Find the index of the first space
# print(text[index+1:])
# print(text.rsplit(maxsplit=1)[1])

# תרגיל 4 שקופית 22
# text = "Toscana"
# print(text[0:4])


# תרגיל 1 שקופית 28
# list1 = ["apple", "banana", "cherry", "melon"]
# print(list1[1])

# תרגיל 2 שקופית 28
# list1 = ["apple", "banana", "cherry", "melon"]
# print(list1[2:])

# תרגיל 3 שקופית 28
# list1 = [7,4,2,9]
# list1.sort()
# print(list1[0])
# print(min([7, 4, 2, 9]))

# תרגיל 4 שקופית 28
# list1 = [7,4,2,9]
# list1.sort(reverse=True)
# print(list1[0])
# print(max([7, 4, 2, 9]))

# תרגיל 5 שקופית 28
# list1 = [7,4,2,9]
# list1.sort(reverse=True)
# print(list1[1])



# תרגיל 1 שקופית 31
# fullName = input("Enter you full name: ")
# print("Good morning, " + fullName.capitalize())

# תרגיל 2 שקופית 31
# fullName = input("Enter you full name: ")
# print(f"My name is {fullName.capitalize()}".replace(" ", "****"))

# תרגיל 3 שקופית 31
# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a number: "))
# print("The result of multiplying the two numbers you chose is: " + str(firstNum * secondNum))



# תרגיל 1 שקופית 41
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# print("Even" if num % 2 == 0 else "Odd")

# תרגיל 2 שקופית 41
# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a number: "))
# print(firstNum if firstNum > secondNum else secondNum)

# if firstNum>secondNum:
#     print(firstNum)
# elif firstNum==secondNum:
#     print("Equal")
# else:
#     print(secondNum)
# print(firstNum) if firstNum > secondNum else print("Equal") if firstNum == secondNum else print(secondNum)

# תרגיל 3 שקופית 41
# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a number: "))
# thirdNum = int(input("Enter a number: "))
# print(firstNum) if (firstNum>secondNum and firstNum>thirdNum) else print(secondNum) if (secondNum>firstNum and secondNum>thirdNum) else print(thirdNum)
# print(max(firstNum, secondNum, thirdNum))

# תרגיל 4 שקופית 41
# num = int(input("Enter a number: "))
# print("Positive") if num > 0 else print("Negative") if num < 0 else print("Zero")
# print(["Zero", "Negative", "Positive"][int(num > 0) + int(num < 0)])

# תרגיל 5 שקופית 41
# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a number: "))
# thirdNum = int(input("Enter a number: "))
# if firstNum < (secondNum+thirdNum) and secondNum < (firstNum+thirdNum) and thirdNum < (firstNum+secondNum):
    # print("A triangle")
# else:
    # print("Not a triangle")
# print("A triangle") if firstNum + secondNum > thirdNum and firstNum + thirdNum > secondNum and secondNum + thirdNum > firstNum else print("Not a triangle")




# תרגיל 1 שקופית 43
# list1 = [2,-4,30,-9,21]
# sum = 0
# for i in list1:
    # sum += i
# print(sum)

# תרגיל 2 שקופית 43
# list1 = [2,-4,30,-9,21]
# multiplicationResult = 0
# for i in list1:
#     if multiplicationResult == 0:
#         multiplicationResult += i
#     else:
#         multiplicationResult *= i
# print(multiplicationResult)

# תרגיל 3 שקופית 43
# list1 = [2,-4,30,-9,21]
# largest_num = max(list1)
# print(largest_num)
# print(max([2,-4,30,-9,21]))


# תרגיל 4 שקופית 43
# list1 = [2,-4,30,-9,21]
# even = 0
# odd = 0
# for i in list1:
#     if i % 2 == 0:
#         even += 1
#     else:
#        odd += 1
# print(f"In the list there is {even} even numbers and {odd} odd numbers.")

# תרגיל 5 שקופית 43
# list1 = [2,-4,30,-9,21]
# list2 = [1,-3,30,-7,20]
# list3 = [13,99,7,-5,9]
# list4 = [1,30,87,-55,91]
# equal = False

# for i in list1:
#     for e in list2:
#         if i == e:
#             equal = True
#             break
# if equal == False:
#     print("false")
# else:
#     print("true")

# list1 = [2, -4, 30, -9, 21]
# list2 = [1, -3, 30, -7, 20]

# if set(list2) & set(list3):
#     print("true")
# else:
#     print("false")
