# 1. Function without any arguments and return type
print("add_1")
def add_1():
    a=5
    b=6
    print(a+b)
add_1()

# 2. Function with arguments and without return type
print("add_2")
def add_2(a,b):
    print(a+b)
add_2(2,3)
# 3. Function without any arguments and with return type
print("add_3")
def add_3():
    a=8
    b=9
    return a+b
addition=add_3()
print(addition)
# 4. Function with any arguments and return type
print("add_4")
def add_4(a,b):
    return a+b
addition=add_4(3,4)
print(addition)
