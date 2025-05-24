class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name #public
        self._salary = salary # private
        self.__ssn = ssn #protected

emp = Employee("Safa", 90000, "0123456789")

print(emp.name)
print(emp._salary)
print(emp.__ssn)



        