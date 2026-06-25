# Model
class Student:

    def __init__(self, name):
        self.name = name


# View
class StudentView:

    def show(self, student):
        print(student.name)


# Controller
class StudentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update(self):
        self.view.show(self.model)


student = Student("Alice")

view = StudentView()

controller = StudentController(student, view)

controller.update()