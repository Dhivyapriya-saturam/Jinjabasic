class Employee:
    empcount = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Employee.empcount += 1

    def display(self):
        """This displays the name and id of the employees
        """
        print("Name:", self.name, "Id:", self.id)


emp1 = Employee("Dhivya", 1)
emp2 = Employee("Priya", 2)
emp1.display()
emp2.display()
print("Total Employee %d" % Employee.empcount)
