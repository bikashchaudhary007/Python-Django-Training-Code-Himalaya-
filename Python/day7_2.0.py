import random

class Employee:
    def __init__(self, name, emp_code, designation):
        self.name = name
        self.emp_code = emp_code
        self.designation = designation
    
        
    @staticmethod
    def rand_emp_code():
        r1 = random.randint(1000, 9999)
        return r1
    
    @classmethod
    def emp_details(cls,name,designation):
        # print("Emp Code: ", emp_code)
        emp_code = cls.rand_emp_code()
        return cls(name,emp_code,designation)


Emp2 = Employee.emp_details("Bikash Chaudhary","Manager")
print(f'Employee Details: \n{Emp2.name}, \n{Emp2.emp_code}, \n{Emp2.designation}')