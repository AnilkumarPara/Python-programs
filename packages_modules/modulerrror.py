try:
    from arthematic_functions import add1
    print(add1(2,3))
except ImportError:
    print("Module name is not found")
