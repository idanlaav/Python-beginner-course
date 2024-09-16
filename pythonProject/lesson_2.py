# print("#" * 50)

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

# for a in range(5, 0, -1):
#     for b in range(a , 0 , -1):
#         print(b, end=" ")
#     print()


# sum = 0
# for i in range(5):
#     currentNumber = int(input("Enter a positive number or zero to quit: "))
#     if currentNumber == 0:
#         break
#     elif currentNumber < 0:
#         print("You can't insert a negative number.")
#         break
#     else:
#         sum += currentNumber
# print(sum)


# userNumber = int(input("Enter a positive number or zero to quit: "))
# for num in range(2,userNumber):
#     if userNumber % num == 0:
#         print("Not a primary number.")
#         break
# else:
#     print("Primary number")


# continue = if it's correct it will start again the loop
# x = "0"
# total = 0
# while x.isdigit():
#     x = input("Enter a number or any other character to quit: ")
#     if x == "7":
#         continue
#     print(x)


# pass = can ignore from write something
# for i in range(5):
#     pass
# x = 3
# y = 5
# if x > y:
#     print(x)
# elif x == y:
#     pass
# else:
#     pass


# x = 5
# y = 3
# while x > y:
#     y += 1
#     print("Hello")


# if the string is between 0-9 its true = isdigit
# x = "0"
# total = 0
# while x.isdigit():
#     x = input("Enter a number or any other character to quit: ")
#     print(x)


# like json
# student1 = {"name":"john","age":30,"is_student":True,"grades":[76,87,97]}
# print(student1)
# print(student1["age"])


# if there is two arguments with another value it will save only the last one in the position of the first one
# student1 = {"name":"john","age":30,"is_student":True,"grades":[76,87,97],"age":40}
# print(student1)

# student1 = {"name":"john","age":30,"is_student":True,"grades":[76,87,97]}
# student1["age"] = 31
# print(student1)


# student1 = {"name":"john","age":30,"is_student":True,"grades":[76,87,97]}
# print(student1["city"]) # error key doesn't exist
# print(student1.get("city")) # if there is no key it will print none, if its exist it will print the key

# if student1.get("city") != None:
#     pass

# adding to the list
# student1["city"] = "Tel Aviv"
# print(student1)


# for i  in student1.keys():
# print(i) # print all the keys
# print(i, student1[i]) # print all the keys and the values
# print(f"{i}={student1[i]}")


# for i in student1.values():
#     print(i)


# for i in student1.items():
# print(i)
# print(f"{i[0]}={i[1]}")


# for k,v in student1.items():
#     print(f"{k}={v}")


# print(student1.get("city"))
# print(student1.setdefault("city", "New York")) # if there is no key of city it will insert this key if its exist it will do nothing
# print(student1)


# student_1 = {"name":"john","age":30,"grades":[76,87,97]}
# student_2 = {"name":"paul","age":27,"grades":[88,89,97]}
# student_3 = {"name":"george","age":31,"grades":[85,95,88]}
# students = [student_1,student_2,student_3]

# total_age = 0
# for i in students:
#     total_age += i["age"]
#
# print(total_age/len(students))


# total_grades = 0
# count_grades = 0
# for student in students:
#     for grade in student["grades"]:
#         total_grades += grade
#         count_grades += 1
#
# print(total_grades/count_grades)

# grades = [grade for student in students for grade in student["grades"]]
# print(grades)
# print(sum(grades)/len(grades))



# functions
# print()
# input()
# len()
# sum()
# min()
# max()




# it's not dictionary, it's type set
# in set there is not duplicates like dictionary
# x = {5,6,7,8,9,9,9,8}
# print(x)
# print(list(x))

# x = [5,6,7,8,9,9,9,8]
# print(list(set(x)))


# jan = [5,6,7,8,9,9,9,8]
# feb = [6,8,4,4]
# print(set(jan).intersection(feb)) # show what is the same items between the sets
# print(set(jan).difference(feb)) # the difference between the jan to feb without feb
# print(set(feb).difference(jan)) # the difference between feb jan to feb without jan
# print(set(jan).union(feb)) # all the items from two of them
# print(set(jan).symmetric_difference(feb)) # all the items that not exist in them together



# def is definition of function
# def greeting():
#     print("Hello")
# greeting()

# def avg(x,y):
#     return (x+y) / 2
# print(avg(5,9))

# def greeting(name):
#     return f"Hello, {name}"
# print(greeting("Idan"))

# def greeting(name, lang):
#     if lang == "esp":
#         return f"Hola, {name}"
#     else:
#         return f"Hello, {name}"
# print(greeting("Idan", "Laav"))
# print(greeting("Idan", "esp"))

# after parm with default value we can only add another parm with default value
# def greeting(name, lang="eng"):
#     if lang == "esp":
#         return f"Hola, {name}"
#     else:
#         return f"Hello, {name}"
# print(greeting("Idan", "Laav"))
# print(greeting("Idan"))

# work
# def greeting(name, lang="eng", age=0):
# doesnt work
# def greeting(name, lang="eng"):

# def greeting(name,age, lang="eng"):
#     if lang == "esp":
#         return f"Hola, {name}"
#     else:
#         return f"Hello, {name}"
# can write where ever I want but i have to write the keys of everyone
# print(greeting(age=30, name="Idan", lang="Laav"))
# print(greeting(age=30, name="Idan")) # lang is still with default value it's ok to not write this parm


# def greeting(name,age, lang="eng"):
#     dict1 = {"eng":"Hello","esp":"Hola","heb":"שלום"}
#     return f"{dict1[lang]}, {name}"
# print(greeting(age=30, name="Idan", lang="esp"))


# can insert how many parm i want
# def avg(*args):
#     return sum(args)/len(args)
# print(avg(5,7,8,9,12,33))


# make all the arguments into a dictionary
# def get_student(**kwargs):
#    return kwargs
# print(get_student(name="john",age=30,grades=[88,77,88]))


# students = []
# def add_student(**kwargs):
#     students.append(kwargs)
# add_student(name="john",age=30,grades=[88,77,88])
# add_student(name="paul",age=32)
# print(students)



