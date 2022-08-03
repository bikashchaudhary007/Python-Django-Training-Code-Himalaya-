'''
Python Training Day 7
Create a class Employee, with attributes: name, emp_code, designation.
Generate 4 digit emp code (using static method)
Create a method to create an employee object and emp_code for it should be generated using the method: that you created in Q.3.a.
Create objects :
One directly by passing parameters to the class. 
Another by the method you created in Q.3.b.
'''
import random

class Employee:
    def __init__(self, name, emp_code, designation):
        self.name = name
        self.emp_code = emp_code
        self.designation = designation
    
    # def __str__(self):
    #     return f'Employee details: name: {self.name}, emp_code: {self.emp_code}, designation: {self.designation}'
    
    def get_details(self):
        print("Name:",self.name)
        print("Emp_code:", self.emp_code)
        print("Designation:",self.designation)
        
    @staticmethod
    def rand_emp_code():
        r1 = random.randint(1000, 9999)
        print("Random Code: ",r1)
        return r1

code = Employee.rand_emp_code()
Emp1 = Employee("Bikash",code,"Manager")
Employee.get_details(Emp1)



