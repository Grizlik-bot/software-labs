from visitable import Visitable

class Department(Visitable):
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_name(self):
        return self.name

    def get_employees(self):
        return self.employees

    def accept(self, visitor):
        visitor.visit_department(self)
