# parent class
class Person(object):
    #__init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# Creation of an object variable or an instance
a = Employee("David", 133707, 10000000, "Intern")

# Calling a function of the class Person using its instance
a.display()