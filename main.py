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
        super().__init__(name, age, gender, student_id, course)
        self.student_id = student_id
        self.grades = []
        self.avg = 0
    
    def set_student_details(self):
        self.student_id = input("Please enter your student id - ")
        self.course = input("Please enter your course - ")
    
    def add_grade(self):
        grade = (input("Please enter your new grade - "))
        self.grades.append(grade)
    
    def calcavg(self):
        self.avg = (sum(int(self.grades)) / len(self.grades))
        print(f"{self.avg} is your average grade")
    
    def get_summary(self):
        print(f"Your name is {self.name}")
        print(f"Your student id is {self.student_id}")
        print(f"Your average grade is {self.avg}")
        print(f"Your course is {self.course}")

human = Person("Jokubas", 16, "Male")
stu = Student(Person, "S1234", "Engineering")
stu.get_summary()



