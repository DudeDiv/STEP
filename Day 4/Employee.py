from datetime import date

class Company:
    def __init__(self, name, dt_inc):
        self.name = name
        self.dt_inc = dt_inc
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            employee.set_company(self)
        else:
            raise TypeError("Can only add Employee objects")

    def get_name(self):
        return self.name

    def get_dt_inc(self):
        return self.dt_inc

    def get_employees(self):
        return self.employees

class Employee:
    def __init__(self):
        self.emp_id = ""
        self.name = ""
        self.address = None
        self.company = None

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def get_emp_id(self):
        return self.emp_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_company(self, company):
        self.company = company

    def get_company(self):
        return self.company

class Address:
    def __init__(self):
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.pin_code = ""

    def get_line1(self):
        return self.line1

    def set_line1(self, line1):
        self.line1 = line1

    def get_line2(self):
        return self.line2

    def set_line2(self, line2):
        self.line2 = line2

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_pin_code(self):
        return self.pin_code

    def set_pin_code(self, pin_code):
        self.pin_code = pin_code

class DisplayForm:
    def display_employee(self, emp):
        print("\nEmployee Details:")
        print("Emp ID :", emp.get_emp_id())
        print("Name :", emp.get_name())
        print("Line 1 :", emp.get_address().get_line1())
        print("Line 2 :", emp.get_address().get_line2())
        print("City :", emp.get_address().get_city())
        print("PinCode :", emp.get_address().get_pin_code())
        print("Company :", emp.get_company().get_name())
        print("Company Incorporation Date :", emp.get_company().get_dt_inc())

def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            year, month, day = map(int, date_str.split('-'))
            return date(year, month, day)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    # Get Company input
    company_name = input("Enter company name: ")
    company_inc_date = get_date_input("Enter company incorporation date (YYYY-MM-DD): ")
    company = Company(company_name, company_inc_date)

    # Get Employee input
    emp = Employee()
    emp.set_emp_id(input("Enter employee ID: "))
    emp.set_name(input("Enter employee name: "))

    # Get Address input
    a1 = Address()
    a1.set_line1(input("Enter address line 1: "))
    a1.set_line2(input("Enter address line 2: "))
    a1.set_city(input("Enter city: "))
    a1.set_pin_code(input("Enter pin code: "))

    # Set employee's address
    emp.set_address(a1)

    # Add employee to the company
    company.add_employee(emp)

    # Display employee information
    form = DisplayForm()
    form.display_employee(emp)
