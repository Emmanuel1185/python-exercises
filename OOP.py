#20/01/25: object oriented programming
#object= instance of a class which contains data and methods
#class = blueprint
# myName is an object


# class Fruits:
#     def __init__(self, name, colour, taste, shape):
#         self.name = name
#         self.colour = colour
#         self.taste = taste
#         self.shape = shape
#     def printHealthyFood(self):
#         print(f"{self.name} are {self.colour}, {self.taste} and {self.shape}")

# fruit1 = Fruits ("Apples", "red", "sweet", "round")
# fruit2 = Fruits ("Oranges", "orange", "sour", "round")
# fruit3 = Fruits ("Bananas", "yellow", "sweet", "straight")

# fruit2.printHealthyFood()

from student_module import student

student_1 = student ("Emmanuel","Adefemi", "39", "Science")
student_1.printFullName()
student_1.printage()
student_1.printdepartment()



