# פקודה צבועה בסגול היא פקודה מוכרת
# ctrl + shift and חצים moving row down or up


# דוגמה1
# print("hello world")


# הסבר על סוגי מספרים
# 123 int # מספר רגיל
# 12.3 float # מספר עם שבר
# 1j complex # מספר מסובך



#חישוב עם מספרים לא שלמים דוגמה 2
# x = 3
# y = 4.2
#
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)



# דוגמה 3
# x = 3
# y = 4

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x**y) # חזקה
# print(x//y) # מחלקים ומעגלים למטה למספר שלם
# print(x%y) # שארית


# תרגיל 1
# pi = 3.14159
# radius = 12
# sum = pi*radius*2
# print(pi*radius**2)



# x += 1
# x -= 1
# x *= 2
# x /= 2



# ביטויים בוליאנים סימנים
# x = 3
# y = 3
# print(x >= y) # < <= == !=
# print(x>y and x>10 or y==5) # ״אנד״ חזק יותר מ ״אור״
# print(2<=x<=5) # ניתן להוסיף נוט ("not") לבדוק אם זה לא נכון
# x = 100_000_000 # מתעלם מהמקפים התחתונים וקורא את זה כמספר רגיל (נוח לעיניים)

# x = 101_202_303_404
# print(x)


# string start in "" or ''
# "hello"
# 'hello2'
# there is a string with """ its a multy line example: (we can write \n too), \t??
# print("""sadasd
# asdasda
# asdas
# dasd
# """)

# x = """idan
# agam
# omer
# iris"""
# print(x)


# with path we have to use r in the start of the path to ignore \ in the line of the path
path = r"c:\new\templates\black\david"
# print(path)



# print("hello" + "world")
# print("*" * 50)


# make an input and waiting while you end to answer before display the second one
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")



# תרגיל 2 להדפיס שם פרטי ושם משפחה לאחר האינפוטים
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")

# There is two option to write, the second is better
# print("Hello, " + fname + " " + lname)
# print(f"Hello, {fname} {lname}")
# print(f"The first character in your last name is {lname[0]}")

# חישוב האות האחרונה בשם
# print(f"The last character in your first name is {lname[-1]}") # -1 is from the end, -2 is 2  from the end


# print("Hello".upper()) # אותיות גדולות


# להכין שלאחר הקלדה של היוזר האות הראשונה בשם תיהיה גדולה
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")

# print(f"Hello, {fname.capitalize()} {lname.capitalize()}") # אות ראשונה אות גדולה

# check it
# print(f"Hello, {fname[0].upper()}{fname[1:]} {lname[0].upper}{lname[1:]}") # אות ראשונה אות גדולה




# text = "Hello world"
# print(text[2:5]) # print from the first num to the last num without him
# print(text[2:]) # print from the first num to the end - slicing
# print(text[0:6:2])
# print(text[::-1]) # from the end to the start



# תרגיל - שיוזר יקליד טקסט ולהדפיס נכון או לא נכון האם הטקסט שהוא הקליד פלידרום (האם ניתן להקליד אותו מהסוף להתחלה)
# text = input("Enter text:")
# print(text == text[::-1])


# There is no Array in Python it's called "list"
# x = [5,True,"Hello",[3,4,5]]
# print(x[-1][1]) # print array in position 1


# x = [5,True,"Hello",[3,4,5]]
# print(x[-1][:2])
# print(x[-1][0:2]) # [0:2] = [:2]


# y = [3,5,7]
# y.append(5) # append = push
# y.append(6) # append = push
# y.insert(0,11) # the first number is the position where to add the second is the number to add
# y.insert(2,15)
# y.pop(-2) # remove position 2

# print(y)


# y = [3,15,7, 9]
# y.sort() # by the small to the big
# y.sort(reverse=True) # by the big to the small
# print(y)


# y = [3,15,7,9]
# x = [5,6,7,8,9]
# y.sort(reverse=True)
# print(x+y)


# age = input("Enter your age")
# print("Next year you will be " + age + 1) # = Error

# age = int(input("Enter your age: "))
# print("Next year you will be " + str(age + 1)) # = success
# print(f"Next year you will be {age + 1}") # = success



# x = [5,6,7] # list
# y = (5,6,7) # tuple
# z = 9,8,7 # tuple

# tuple like list but he is immutable, read only
# mutable: list
# immutable: tuple, str, int, boolean

# mutable
# x = [4,5,6]
# x[1] = 8
# print(x)

# immutable
# x = "Hello"
# x[1] = "a"
# print(x)

# replace build a new argument
# x = "Hello"
# y = x.replace("e", "ok")
# print(y)



# x,y,z = 5,6,7 # x = 5, y = 6, z = 7
# print(y)


# x,y,*z = 5,6,7,8,9,10 # * says that z = list of the z position to the end
# print(z)


# x,*y,z = 5,6,7,8,9,10 # * says that y = list of the y position to z without z
# print(y)


# x = 5
# y = 6
#
# תנאי (:={})
# if x > y:
#     print(x)
#     # print(x)
# elif x == y:
#     print("=")
# else:
#     print(y)

# print(x if x > y else y)





# לולאות
# דוגמה אחת
# for i in "hello":
#     print(i)

# דוגמה שנייה
# list = [1,2,3,4,5,7]
# for i in list:
#     print(i)

# דוגמה שלישית
# for i in range(5):
#     print(i)

# דוגמה רביעית
# for i in range(2,7): # print from 2 to 6
#     print(i)

# דוגמה חמישית
# for i in range(1,6,2): # print form 1 to 5 up two numbers
#     print(i)

# דוגמה שישית
# for i in range(6,1,-1):
#     print(i)


# תרגיל להדפיס מ 5 עד 1
# for i in range(5,0,-1):
#     print(i)
# print("boom")


# list1 = [5,8,13,15,18]
# for i in list1:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("לא זוגי")


# list1 = [5,8,13,15,18]
# for i in list1:
#     if i % 2:
#         print(i)
#     else:
#         print("זוגי")


# list1 = [5,8,13,15,18]
# sum = 0
# for i in list1:
#     if i % 2 == 0:
#         sum += i
# print(sum)



# long way
# list1 = [5,8,13,15,18]
# even = []
# for i in list1:
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# short way
# list1 = [5,8,13,15,18]
# print([i for i in list1 if i % 2 == 0])



