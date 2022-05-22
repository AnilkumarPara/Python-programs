class Employee:
    employee_name='Billgates'
    empl_sal=10000

emp1=Employee()

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

