from visitable import Visitable

class Company(Visitable):
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def get_name(self):
        return self.name

    def get_departments(self):
        return self.departments

    def accept(self, visitor):
        visitor.visit_company(self)
        for department in self.departments:
            department.accept(visitor)
