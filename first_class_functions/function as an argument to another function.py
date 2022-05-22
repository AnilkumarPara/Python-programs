def divisible_2(number):
    if number%2==0:
        return True
    else:
        return False



# Pass function as an argument to another function
print("--Pass function as an argument to another function--")
def my_map(func,numbers):
    result=[]
    for n in numbers:
        result.append(func(n))
    print(result)

my_map(divisible_2,[2,3,4,5,6,7])



print(divisible_2)
print(my_map)
