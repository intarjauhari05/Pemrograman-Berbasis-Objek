class Person():
    def __init__(self, name='', date_of_birth='', parents='', children=''):
        self.name = name
        self.date_of_birth = date_of_birth
        self.parents = parents
        self.children = children

class Student(Person):
    def __init__(self, student_ID='', name='', date_of_birth='', parents='', children=''):
        super().__init__(name, date_of_birth, parents, children)
        self.student_ID = student_ID

class Employee(Person):
    def __init__(self, employee_ID='', name='', date_of_birth='', parents='', children=''):
        super().__init__(name, date_of_birth, parents, children)
        self.employee_ID = employee_ID