# Overriding example
from arithmetic_operations import addition as add1
def addition(x,y):
    print("I am in the override file")
    return x+y

add=add1(2,3)
print('add=',add)


sum=addition(2,4)
print('sum=',sum)

