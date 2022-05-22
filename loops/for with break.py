# WAP to search a given element is available in the list
import time
l=[2,3,4,5,7,21,43]
search_element=int(input("enter the search element"))
start=time.time()
for i in l:
    if i == search_element:
        print(search_element,"is found")
end=time.time()
print("time taken without a break=",end-start)


start=time.time()
for i in l:
    if i == search_element:
        print(search_element,"is found")
        break
end=time.time()
print("time taken with a break=",end-start)
