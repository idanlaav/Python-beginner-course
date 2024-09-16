# from lesson_4 import Point
# p1 = Point(4,5)
# p2 = Point(5,6)
# print(p1>p2)

# from lesson_4 import Point
# class ColoredPoint(Point):
#     def set_color(self,color):
#         self.color = color
#     def __str__(self):
#         return  super().__str__() + f" and my color is {self.color}."
#
# p1 = ColoredPoint(5,6)
# p1.set_color("Green")
# print(p1)



# from lesson_4 import Point
# class ColoredPoint(Point):
#     """ some comment that we want to share while the user will use help"""
#     def __init__(self,x,y,color):
#         super().__init__(x,y)
#         self.color = color
#     def __str__(self):
#         return  super().__str__() + f" and my color is {self.color}."
#
# p1 = ColoredPoint(5,6, "Green")
# print(p1)
# help(ColoredPoint)



# in this code we can show that we can get the super of two class, this code doesn't working, it's only to explain
# from lesson_4 import Point
# class ColoredObject():
#     def __init__(self,color):
#         self.color = color
#     def __str__(self):
#         return  super().__str__()
# class ColoredPoint(ColoredObject,Point):
#     """ some comment that we want to share while the user will use help"""
#     def __init__(self, x, y, color):
#         super().__init__(x, y)
#         self.color = color
#
#     def __str__(self):
#         return super().__str__() + f" and my color is {self.color}."
#
# p1 = ColoredPoint(5, 6, "Green")
# help(ColoredPoint)



