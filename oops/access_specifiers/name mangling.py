class Parent:
    def __mangling(self):
        pass
    def __mangling_(self):
        pass
    def __mangling__(self):
        pass
p=Parent()
print(dir(p))
