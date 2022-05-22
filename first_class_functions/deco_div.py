def deco(func):
    print("deco function")
    print("func=",func)
    def my_map(numbers):
        print("I am in my_map functtion")
        result=[]
        for n in numbers:
            result.append(func(n))
        print(result)
    print("my_map=",my_map)
    return my_map

@deco
def divisible_2(number):
    print("I am in divisible_2")
    if number%2==0:
        return True
    else:
        return False



divisible_2([1,2,3,4])


#print("before divisible_2=",divisible_2)

#divisible_2=deco(divisible_2)
#print("after divisible_2=",divisible_2)
