class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      : ₹", self.salary)
        print("Category    :", self.category())
        print()


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if len(self.employees) == 0:
            print("No employee records available.")
        else:
            print("\nEmployee Details")
            print("----------------")
            for employee in self.employees:
                employee.display()


company = Company()

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter details of Employee", i + 1)
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    salary = float(input("Salary: "))
    company.add_employee(Employee(emp_id, name, salary))

company.display_employees()