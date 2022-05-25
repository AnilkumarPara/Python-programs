class Parent:
    a=5
    def __init__(self,c):
        print("I am in the parent init method")
        self.c=c
        
    def display(self):
        print("I am in the parent display method")
        print("Value of 'a' from the parent class",self.a)
        print("Value of 'c' from the parent class",self.c)


class Child(Parent):
    a=50
    b=6
    def __init__(self,d):
        print("I am in the child init method")
        self.d=d
    
    def display(self):
        print("I am in the child display method")
        print("Value of 'a' from the child class",self.a)
        print("Value of 'b' from the child class",self.b)
        #print("Value of 'c' from the child class",self.c)
        print("Value of 'd' from the child class",self.d)

p=Parent(30)
c=Child(40)
p.display()
print()
c.display()

