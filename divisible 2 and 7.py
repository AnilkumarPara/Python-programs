# WAP to find number which is divisible by 2 and 7 from the list of numbers

numbers=[2,8,21,14,34,100,105]

print("---using for loop---")

div_2_7=[]
for number in numbers:
    if number%2==0:
        if number%7==0:
            div_2_7.append(number)

print(div_2_7)

print("---using List Comprehension---")
divisble_2_7 = [number for number in numbers if number%2==0  if number%7==0]
print(divisble_2_7)

