# WAP to find the greatest 4 numbers using nested if
import time
a,b,c,d=1,2,3,4
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
start=time.time()
print("--- Program of nested if ----")
if a>b:
    if a>c:
        if a>d:
            print("a is greatest of all the numbers")
        else:
            print("d is greatest of all the numbers")
    else:
        if c>d:
            print("c is greatest of all the numbers")
        else:
            print("d is greatest of all the numbers")
elif b>c:
    if b>d:
            print("b is greatest of all the numbers")
    else:
            print("d is greatest of all the numbers")
elif c>d:
    print("c is greatest of all the numbers")
else:
        print("d is greatest of all the numbers")

end=time.time()
print("Total execution time=",end-start)
print("--- End of the Program ----")
