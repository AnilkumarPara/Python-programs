def add(**kwargs):
    print(kwargs)
    print(*kwargs)
    #print(**kwargs)
    
    sum=0
    for key,value in kwargs.items():
        print(key,value)
        sum=sum+value
    print("sum=",sum)
    

add(a=2,b=3)


