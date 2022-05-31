class Parent:
    a=5
    
        
        
    def display(self):
        print("I am in the Parent display method")
        print("Value of 'a' from the Parent class",self.a)

class Child1(Parent):
    b=6
    

class Child2(Parent):
    c=7
    def __init__(self):
        print("init start in Child2")
        
        
    def display(self):
        print("I am in the Child2 display method")
        print("Value of 'a' from the Parent class",self.a)
        print("Value of 'c' from the Child2 class",self.c)
c1=Child1()
c2=Child2()

print("---------Child1------------------")
c1.display()
print("---------Child2------------------")
c2.display()

p=Parent()
print("---------Parent------------------")
p.display()
