def deco(func):
    def my_map(numbers):
        result=[]
        for n in numbers:
            result.append(func(n))
        print(result)
    return my_map

@deco
def divisible_2(number):
    if number%2==0:
        return True
    else:
        return False
divisible_2([1,2,3])
#my_map=deco(divisible_2)
#my_map([1,2,3])
@deco
def divisible_7(number):
    if number%7==0:
        return True
    else:
        return False
divisible_7([1,2,3,14])
