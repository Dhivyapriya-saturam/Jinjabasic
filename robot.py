class Robot:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def introduce_self(self):
        """Displaying the name and dept of the user
        """
        print("My name is" + " " + self.name)
        print("I am from" + " " + self.dept + " " + "dept")


r1 = Robot("Dhivya", "IT")
r2 = Robot("Priya", "CT")
r1.introduce_self()
r2.introduce_self()
