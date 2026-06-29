'''Requirements:
Create an abstract class Person.
Attributes: name, age
Abstract method: display_info()
Create two child classes:
Student
Teacher
Student should have:
roll_no
private attribute __marks
methods:
getter and setter for marks
override display_info()
method to calculate grade:
90+ → A
75-89 → B
60-74 → C
below 60 → Fail
Teacher should have:
subject
salary
override display_info()
Create another class Department.
class variable → university_name = "XYZ University"
store multiple students and teachers.
methods:
add_student()
add_teacher()
show_all_members()

Create at least:
3 students
2 teachers
Display complete details.'''

from abc import ABC,abstractmethod

class person(ABC):
    @abstractmethod

    def display_info(self):
        pass

class student(person):

    def __init__(self,name,age,roll_no,marks):
        self.name = name
        self.age = age
        self.__marks = marks
        self.roll_no = roll_no

    def get_marks(self):
        return self.__marks
    
    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75 and self.__marks <= 89:
            return "B"
        elif self.__marks >= 60 and self.__marks <= 74:
            return "C"
        else :
            return "Fail"
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll No : {self.roll_no}")
        print(f"Grade : {self.grade()}")
        

s = student("John", 20, "S123", 85)
s.display_info()




class teacher(person):
    def __init__(self,name,age,subject,salary):
        self.name = name
        self.age = age
        self.subject = subject
        self.salary = salary
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Subject : {self.subject}")
        print(f"Salary : {self.salary}")

class department:
    university_name = "XYZ University"
    def __init__(self):
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)

    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    
    def show_all_members(self):
        print("Students:")
        for student in self.students:
            student.display_info()
        print("\nTeachers:")
        for teacher in self.teachers:
            teacher.display_info()

s1 = student("John",20,"S123",85)
s2 = student("Arnav",18,"S124",95)

t1 = teacher("Rahul",35,"Python",50000)
t2 = teacher("Priya",40,"Java",60000)

dept = department()

dept.add_student(s1)
dept.add_student(s2)

dept.add_teacher(t1)
dept.add_teacher(t2)
dept.show_all_members()