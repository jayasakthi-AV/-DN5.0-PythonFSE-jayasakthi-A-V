class Student:
    def __init__(self, name):
        self.name = name


class StudentRepository:
    def save(self, student):
        print(f"Saving {student.name} to database")


class EmailService:
    def send(self, student):
        print(f"Email sent to {student.name}")


student = Student("John")

repo = StudentRepository()
repo.save(student)

email = EmailService()
email.send(student)