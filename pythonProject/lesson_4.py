# class Point():
#     def __init__(self): // happened auto without call it
#         print("Object created.")
#     def show(self):
#         print("I am a point.")
#
# x = int()
# s = str()
# p = Point()
# p.show()



# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"I am a point ({self.x},{self.y}).")
#
# p1 = Point(x=5,y=9)
# p1.show()



# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"I am a point ({self.x},{self.y})."
#
# p2 = Point(x=5,y=9)
# print(p2)


# class Point(object): # dont use it - example that we can use object
# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"I am a point ({self.x},{self.y})."
#     def __gt__(self, other):
#         return self.x**2 + self.y**2 > other.x**2 + other.y**2
# # if we don't run this current file the main of this class will not display while the user will be using import
# if __name__ == "__main__":
#     p3 = Point(x=5,y=9)
#     p4 = Point(x=-1,y=12)
#     print(p3>p4)
#     x = 3
#     y = 5
#     print(x.__gt__(y))
# p1 = Point(4,5)


