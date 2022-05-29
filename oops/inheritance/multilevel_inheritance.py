class GrandParent:
    a=5
    def __init__(self):
        print("I am in the GrandParent init method")
        
        
    def display(self):
        print("I am in the GrandParent display method")
        print("Value of 'a' from the GrandParent class",self.a)

class Parent(GrandParent):
    b=6
    def __init__(self):
        print("I am in the Parent init method")
        
        
    def display(self):
        print("I am in the Parent display method")
        print("Value of 'a' from the GrandParent class",self.a)
        print("Value of 'a' from the Parent class",self.b)

class Child(Parent):
    c=7
    def __init__(self):
        print("init start in Child")
        
        
    def display(self):
        print("I am in the Child display method")
        print("Value of 'a' from the GrandParent class",self.a)
        print("Value of 'b' from the Parent class",self.b)
        print("Value of 'c' from the Child class",self.c)

c=Child()
c.display()
