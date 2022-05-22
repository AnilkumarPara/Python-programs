from arithmetic_operations import *
# here also overriding can happen

def subtraction(x,y):
    print("---subtraction function from the start import file---")
    return x-y

def division(x,y):
    print("---division function from start import file---")
    if y==0:
        return 'divisor shouldnot be 0'
    else:
        return x/y


print("sum=",addition(2,3))
print("subtraction=", subtraction(2,3))
print("multiplication=", multiplication(2,3))
print("division=", division(2,3))
