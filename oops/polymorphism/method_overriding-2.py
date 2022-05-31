class Parent:
    a=5
    def display(self):
        print("Printing the Parent variable a=", self.a)

class Child(Parent):
    a=6
    def display(self):
        print("Printing the Child variable a=", self.a)
c=Child()
c.display()
