# syntax of import
# import modulename

'''
# Example
import arithmetic_operations
sum=Arithmetic_Operations.addition(2,3)
print('sum=',sum)

# If you want import more than 1 level then the syntax is follows because in import can have only one level

from modulename import objectname
#or
from package1 import modulename
'''
print("----------------------")
from arithmetic_operations import addition
add=addition(2,3)
print('add=',add)


# Not possible have more than 1 level in the import
#import arithmetic_operations.addition

