 # global variable
def outer():
    print("I am in outer function")
    msg='Hi'
    #print(msg)
    def inner():
        print("I am in inner function")
        print(msg)
    return inner


inner_id=outer()
inner_id()



