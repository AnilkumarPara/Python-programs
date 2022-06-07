class Parent:
    a=5
    __c=7

    def __display3():
        print("I am in Parent __display3")

class Child(Parent):
    a=6
    __c=8

    def __display3():
        print("I am in Child __display3")

print(dir(Child))


# Explain how overriding happens when you have a in both the Parent and Child classes
