# WAP to find the given number is prime or not 

n=int(input("enter a number"))

i=1
count=0
while(i<=n):
    if n%i==0:
        count=count+1
    i=i+1
print("i=",i)
print("count=",count)
print("n=",n)
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")


    
