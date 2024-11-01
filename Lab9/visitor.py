from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_company(self, company):
        pass

    @abstractmethod
    def visit_department(self, department):
        pass

class SalaryReportVisitor(Visitor):
    def visit_company(self, company):
        print(f"Salary report for company: {company.get_name()}")

    def visit_department(self, department):
        print(f"Salary report for department: {department.get_name()}")
