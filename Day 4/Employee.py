class Employee:
    def __init__(self):
        self.emp_id = ""
        self.name = ""
        self.address = None

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
        print("Emp ID :", emp.get_emp_id())
        print("Name :", emp.get_name())
        print("Line 1 :", emp.get_address().get_line1())
        print("Line 2 :", emp.get_address().get_line2())
        print("City :", emp.get_address().get_city())
        print("PinCode :", emp.get_address().get_pin_code())


if __name__ == "__main__":
    emp = Employee()
    emp.set_emp_id("1001")
    emp.set_name("Mayank")

    a1 = Address()
    a1.set_line1("11, SRM TP ")
    a1.set_line2("New Campus  Road ")
    a1.set_city("Chennai")
    a1.set_pin_code("600015")

    emp.set_address(a1)  # connect the objects

    form = DisplayForm()
    form.display_employee(emp)
