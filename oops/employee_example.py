class Employee:
    # Class variables
    number_of_employees=0
    def __init__(self,name):
        #print("I am in the init method")
        self.name=name
        #print(self)
        
    

emp1=Employee('Billgates')

emp2=Employee('David')
print("Employee\n", Employee.__dict__)
print("Emp1\n", emp1.__dict__)
print("Emp2\n", emp2.__dict__)

emp1.number_of_employees=1
emp2.number_of_employees=2

print()
print("Employee\n", Employee.__dict__)
print("Emp1\n", emp1.__dict__)
print("Emp2\n", emp2.__dict__)



print(emp1.name)
print(emp2.name)
print("Using class=", Employee.number_of_employees)
print("Using emp1=", emp1.number_of_employees)
print("Using emp2=", emp2.number_of_employees)
emp1.number_of_employees=1
print("Using emp1=", emp1.number_of_employees)

print("Using emp1=", emp2.number_of_employees)

Employee.number_of_employees+=1
print("number_of_employees",Employee.number_of_employees)
print("number_of_employees",emp1.number_of_employees)
emp1.name='Billgates'
emp1.salary=2000
print(emp1.name)
print(emp1.salary)

emp2=Employee()
emp2.name='David'
emp2.salary=3000

print(emp2.name)
print(emp2.salary)



print("--accessing the attributes of a class using the class Employee---")
print(Employee.employee_name)
print(Employee.empl_sal)

print("--accessing the attributes of a Instance using the class Employee---")
print(emp1.employee_name)
print(emp1.empl_sal)


# Changing the attributes using the class
Employee.employee_name='Sachin'
Employee.empl_sal=2000

print("---look at the values of class and object after modifying data with the class---")
print("---class values---")
print(Employee.employee_name)
print(Employee.empl_sal)

print("---Instance values---")
print(emp1.employee_name)
print(emp1.empl_sal)

# Changing the attributes using the object
emp1.employee_name='Sunil'
emp1.empl_sal=3000

print("---look at the values of class and object after modifying data with the Instance---")
print("---class values---")
print(Employee.employee_name)
print(Employee.empl_sal)

print("---Instance values---")
print(emp1.employee_name)
print(emp1.empl_sal)

# Changing the attributes using the class

Employee.employee_name='Tendulkar'
Employee.empl_sal=7000

print("---look at the values of class and instance after modifying data with the class again---")
print("---class values---")
print(Employee.employee_name)
print(Employee.empl_sal)

print("---Instance values---")
print(emp1.employee_name)
print(emp1.empl_sal)

# Changing the attributes using the instance
emp1.employee_name='suresh'
emp1.empl_sal=25000

print("---look at the values of class and object after modifying data with the Instance again---")
print("---class values---")
print(Employee.employee_name)
print(Employee.empl_sal)

print("---Instance values---")
print(emp1.employee_name)
print(emp1.empl_sal)

