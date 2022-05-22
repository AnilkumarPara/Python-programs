def deco(func):
    def recipients(name,institute_name):
        print(f'Hi {name}')
        func()
        print(f'Regards,\n{institute_name}')
    return recipients

@deco
def course_starts():
    print('I am going to start the following courses on 1st June')
    print('Python','Selenium','Testing')
    


course_starts('Sachin','XYZ')
