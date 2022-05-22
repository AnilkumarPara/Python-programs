
# Assign a function to a variable

print("--Assign a function to a variable--")
def divisible_2(number):
    if number%2==0:
        return True
    else:
        return False


f=divisible_2
print(f)
print(f(3))
