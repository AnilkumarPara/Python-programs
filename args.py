def add(*args):
    print(args)
    print(*args)
    sum=0
    for arg in args:
        sum=sum+arg
    print("sum=",sum)

add(2,3,34,5,6,7,9,10,1,12,3,7)


