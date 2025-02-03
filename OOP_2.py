# # Create a class Person with a constructor that takes two parameters firstname and lastname
# class Person:
#     def  __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
# # Create a method print_name that prints the full name
#     def print_name(self):
#         print(f'Name is {self.firstname} {self.lastname}')

   
# # Create a class Student that inherits from Person
# class Student(Person):
#        def  __init__(self, firstname, lastname, studentId):
#         super().__init__(firstname, lastname)# Call the constructor of the parent class
#         self.studentId = studentId
# # Create a method print_studentId that prints the studentId
#        def print_studentId(self):
#             super().print_name
#             print(f'Student Id is {self.studentId}')
       
# # Create an instance of the Student class
# student1 = Student('John', 'Doe', '1234')
# student1.print_name() # Name is John Doe
# student1.print_studentId() # Student Id is 1234


# multi level inheritance
# class Father:
#         def speak(self):
#             print("Father")

# class Mother:
#     def speak(self):
#         print("Mother")
# class Child(Father, Mother): # multiple inheritance
#     def speak(self):
#         print("Child")

# class grandChild(Child): # multi level inheritance
#     pass

#polymorphism

#Agenda
#1. 4 Building blocks of OOP 
#Inheritance in Python - R&D - single level - multi level - multiple inheritance 
#Polymorphism in Python
class Animal:
        def speak(self):
            print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")
class Cow(Animal):
    def speak(self):
        print("Cow moos")
# Let's call those
dog = Dog()
cat = Cat()
cow = Cow()


def animal_speak(animal):
    animal.speak()
animal_speak(dog) # len("dasda") string
animal_speak(cat)  # len(123) integer 
animal_speak(cow)  #len([1,2,3,4,5]) list length
#withdraw method and apply polymorphism for current account and saving account


