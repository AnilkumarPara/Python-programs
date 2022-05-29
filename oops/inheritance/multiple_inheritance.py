class Parent1:
    a=5
    def __init__(self):
        print("I am in the Parent1 init method")
        
        
    def display(self):
        print("I am in the Parent1 display method")
        print("Value of 'a' from the Parent1 class",self.a)

class Parent2:
    a=6
    def __init__(self):
        print("I am in the Parent2 init method")
        
        
    def display(self):
        print("I am in the Parent2 display method")
        print("Value of 'a' from the Parent1 class",self.b)

class Child(Parent1,Parent2):
    c=7
    def __init__(self):
        print("init start in Child")
        
        
    def display(self):
        print("I am in the Child display method")
        print("Value of 'a' from the Parent1 class",self.a)
        #print("Value of 'b' from the Parent2 class",self.b)
        print("Value of 'c' from the Child class",self.c)
        
c=Child()
c.display()
p=Parent1()
