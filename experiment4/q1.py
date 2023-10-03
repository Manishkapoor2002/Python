class Student:
    def __init__(self, roll_no, name, student_class):
        self.roll_no = roll_no
        self.name = name
        self.student_class = student_class

    def display_info(self):
        print(f"Roll Number: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Class: {self.student_class}")

roll_no = input("Enter Roll Number: ")
name = input("Enter Name: ")
student_class = input("Enter Class: ")

student = Student(roll_no, name, student_class)

print("\nStudent Information:")
student.display_info()

