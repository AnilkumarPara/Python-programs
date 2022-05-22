# Overriding example
import arithmetic_operations
def addition(x,y):
    print("I am in the override file")
    return x+y

sum=arithmetic_operations.addition(5,6)
print('sum=',sum)
                              
add=addition(2,3)
print('add=',add)


