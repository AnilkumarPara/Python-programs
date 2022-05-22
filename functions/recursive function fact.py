def factorial(n):
    if n<=0:
        return "factorial can be found for the positive numbers only"
    else:
        return n*factorial(n-1)

fact=factorial(7)
print("factorial=", fact)
