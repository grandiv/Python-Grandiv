class Person(object):
    # Constructor 
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    # here we return true
    def isEmployee(self):
        return True

# Driver code
emp1 = Person("Joni") # An Object of Person
print(emp1.getName(), emp1.isEmployee())

emp2 = Employee("Grandiv") # An Object of Employee
print(emp2.getName(), emp2.isEmployee())