class Parent:
    def __init__(self,a):
        print("inside __init__()")
        self.a=a
    def __call__(self):
        res = 0
        print("inside __call__()")
        print("adding 2 to the value of res")
        res = self.a + 2
        return res

p=Parent(5)
print(p.__dict__)

print(p())
