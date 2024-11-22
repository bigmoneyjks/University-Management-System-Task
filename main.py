class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self):
        name = input("Please enter your name - ")
        age = int(input("Please enter your age - "))
        gender = input("Please enter your gender - ")
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grades = []
        self.avg = 0
    
    def set_student_details(self):
        self.student_id = input("Please enter your new student id - ")
        self.course = input("Please enter your new course - ")
    
    def add_grade(self):
        grade = int(input("Please enter your new grade - "))
        self.grades.append(grade)
    
    def calcavg(self):
        self.avg = (sum(self.grades) / len(self.grades))
        print(f"{self.avg} is your average grade")
    
    def get_summary(self):
        print(f"Your name is {self.name}")
        print(f"Your student id is {self.student_id}")
        print(f"Your grades are {self.grades}")
        self.calcavg()
        print(f"Your average grade is {self.avg}")
        print(f"Your course is {self.course}")

class Professor(Person):
    def __init__(self, name, age, gender, staff_id, dep, sal):
        super().__init__(name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        self.id = staff_id
        self.dep = dep
        self.salary = sal
    
    def set_prof_details(self):
        self.id = input("Please enter your new staff id - ")
        self.dep = input("Please enter your new department - ")
        self.salary = float(input("Please enter your new salary - "))
    
    def give_feedback(self, stu, feedback):
        print(f"Feedback for {stu.name}: {feedback}")
    
    def increase_salary(self, perc):
        self.salary = (self.salary * float(perc / 100)) + self.salary
    
    def prof_summary(self):
        print(f"Your name is {self.name}")
        print(f"Your staff id is {self.id}")
        print(f"Your salary is {self.salary}")
        print(f"Your department is {self.dep}")

class Admin(Person):
    def __init__(self, name, age, gender, admin_id, office, yoe):
        super().__init__(name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        self.id = admin_id
        self.off = office
        self.exp = yoe
    
    def set_admin_details(self):
        self.id = input("Please enter your new admin id - ")
        self.exp = input("Please enter your new years of experience - ")
        self.off = input("Please enter your new office - ")
    
    def increment(self):
        self.exp += 1
    
    def get_admin_summary(self):
        print(f"Your name is {self.name}")
        print(f"Your admin id is {self.id}")
        print(f"Your office is {self.off}")
        print(f"Your years of experience are {self.exp}")

stu1 = Student("Jokubas Kincinas", 16, "Male", "S5421", "Engineering")
stu2 = Student("David Liu", 16, "Male", "S1334", "Economics")
pro1 = Professor("Mr Stoker", 25, "Male", "P1223", "Maths", 32981.67)
pro2 = Professor("Mr Mahdi", 31, "Male", "P7761", "C.S", 37881.90)
admin = Admin("Big Boss", 55, "Female", "A1111", "U31", 16)
stu1.add_grade()
stu1.add_grade()
stu1.add_grade()
stu1.add_grade()
print("-----------------------")
pro1.give_feedback(stu1, "Please stop being so good at everything")
pro2.increase_salary(10)
admin.increment()
print("-----------------------")
stu1.get_summary()
print("-----------------------")
pro2.prof_summary()
print("-----------------------")
admin.get_admin_summary()


