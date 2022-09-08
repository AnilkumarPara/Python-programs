# WAP to square a each number in the list

l1=[2,7,9,21]

print("--- using for loop---")
squares_list=[]
for n in l1:
    squares_list.append(n*n)
print(squares_list)

print("--- using map function---")
print(list(map(lambda n:n*n,l1)))

def square(n):
    return n*n

print(list(map(square,l1)))
