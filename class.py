# Syntax of class
'''
class class_name:
    # attributes
    # Methods
'''
class Employee:
    employee_name='Billgates'
    empl_sal=10000

    '''
    def do_coding():
        print("He is going to design the framework for a certain problem")
    '''
'''
print("class=",Employee)
print("class address=",id(Employee))
emp1=Employee()
print("object=",emp1)
print("object address=",id(emp1))
''''

print("--accessing the attributes of a class using the class Employee---")
print(Employee.employee_name)
print(Employee.empl_sal)


print(emp1.employee_name)
print(emp1.empl_sal)

# Changing the attributes using the class
Employee.employee_name='Sachin'
Employee.empl_sal=2000


print("look at the values of class and object after modifying data with the class")
print(Employee.employee_name)
print(Employee.empl_sal)

print(emp1.employee_name)
print(emp1.empl_sal)


