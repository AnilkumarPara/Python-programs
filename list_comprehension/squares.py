# WAP to square each number in the list
numbers =[1,2,3,4,5,11,12]
print("---using for loop---")

squares=[]
for number in numbers:
    squares.append(number*number)
print(squares)


print("---using List Comprehension---")
squares_num=[number*number for number in numbers]
print(squares_num)
