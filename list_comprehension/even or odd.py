# WAP to find each number is even or odd from the list of numbers
numbers=[2,3,4,21,25,100,205,210]
print("---using for loop---")
even_odd=[]
for number in numbers:
    if number%2==0:
        even_odd.append('even')
    else:
        even_odd.append('odd')
print(even_odd)

print("---using List Comprehension---")
even_odd_num=['even' if number%2==0 else 'odd' for number in numbers]

print(even_odd_num)
