class Parent:
    a=5
    _b=6
    __c=7
    def display(self):
        #print("value of a=", self.a)
        #print("value of b=", self._b)
        print("value of c=", self.__c)


class Child(Parent):
    b=150



p=Parent()
print(dir(p))
print(p._Parent__c)
p.display()

c=Child()
print(c._Parent__c)
