def details_of_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

details_of_person(name='Anil',age=37,City='Bengaluru')


def details_of_person(*args):
    for arg in args:
        print(arg)

details_of_person('Anil',37,'Bengaluru')
