from employee import Employee
from department import Department
from company import Company
from visitor import SalaryReportVisitor

def main():
    employee1 = Employee("First", 70000)
    employee2 = Employee("Second", 700000)

    department = Department("Idle Department", [employee1, employee2])

    company = Company("Nothing Doing Comp", [department])

    salary_report_visitor = SalaryReportVisitor()

    company.accept(salary_report_visitor)

    department.accept(salary_report_visitor)

if __name__ == "__main__":
    main()
