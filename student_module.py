
class student:
    # Constructor - Special method that is called automatically when an object is created.
    def __init__(self, firstName, lastName, age, department):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.department = department
    
    # Methods for the class
    def printFullName(self):
        print(f" {self.firstName} {self.lastName}")

    def printage(self):
        print(f" Age is {self.age}")

    def printdepartment(self):
        print(f" Department is {self.department}")

student_1 = student ("Emmanuel","Adefemi", "39", "Science")# Creating an object of the class

student_1.printFullName()# Calling the method of the class
student_1.printage()
student_1.printdepartment()
