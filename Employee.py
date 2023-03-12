##------------------------------------------------------------
##  Python OOP Tutorial:
##  https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
##------------------------------------------------------------


##--------------------
##  Python example class:
##--------------------
class Employee:
    raise_salary = 1.04


    #--------------------------------------------------------------------------------
    #  Dunder methods: https://docs.python.org/3/reference/datamodel.html#special-method-names
    #--------------------------------------------------------------------------------
    def __init__(self, first, last, salary=0):
        self.first = first
        self.last = last
        self.salary = salary
        print("Object created:", self.fullname)
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.salary})"
    def __str__(self):
        return f"{self.fullname}"
    def __add__(self, other):
        return self.salary + other.salary
    def __del__(self):
        print("No more used => object deleted:",self)

    #--------------------
    #  Instance methods:
    #--------------------
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_salary)

    #--------------------
    #  Instance properties:
    #--------------------
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        print("Set new name:", person.fullname)

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Deleted fullname:",self)


##--------------------
##  Trying out the example class:
##--------------------
print("===== Dunder methods:")
person = Employee("John", "Smith", 50000)
print("Object representation:", repr(person))
print("Object ID:", id(person))


colleague = Employee("Another", "Employee", 60000)
print("Combined salary:", person + colleague)

print("===== Instance properties:")
person.fullname = "Corey Schafer"
del person.fullname
