# WAP to find the greatest 4 numbers using nested if else

a,b,c,d=1,2,3,4
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)

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
else:
    if b>c:
        if b>d:
            print("b is greatest of all the numbers")
        else:
            print("d is greatest of all the numbers")
    else:
        if c>d:
            print("c is greatest of all the numbers")
        else:
            print("d is greatest of all the numbers")
