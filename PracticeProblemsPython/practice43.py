class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetail(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetail()

engg1 = Engineer("Elon Musk", 40)
engg1.showDetail()