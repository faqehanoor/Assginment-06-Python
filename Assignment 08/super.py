class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")

t1 = Teacher("Ms. Ayesha", "Mathematics")

