# Base Class
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show_person(self):

        print("Showing the Name:", self.name)
        print("Showing the Age:", self.age)


# Derived Class
class Student(Person):

    def __init__(self, name, age, roll_no, marks):

        # Calling parent class constructor
        super().__init__(name, age)

        self.roll_no = roll_no
        self.marks = marks

    def show_student(self):

        # Error Handling
        if self.age <= 0:
            print("Invalid Age")
            return

        if self.marks < 0 or self.marks > 100:
            print("Invalid Marks")
            return

        print("\nStudent Details:")
        print("--------------------")

        # Parent class function
        self.show_person()

        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Main Program

name = input("Enter Name: ")

age = int(input("Enter Age: "))

roll_no = input("Enter Roll Number: ")

marks = float(input("Enter Marks: "))

# Object Creation
s1 = Student(name, age, roll_no, marks)

# Function Call
s1.show_student()