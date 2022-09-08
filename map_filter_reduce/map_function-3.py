# Using the function Map, count the number of words that start with ‘S’ in input_list.
city_names = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']

print("--- for loop ----")
counter=0
for city in city_names:
    if city.startswith('S'):
        counter+=1

print("number of city names starts with 'S'=", counter)

print("--- map function ----")
print(sum(map(lambda city:city.startswith('S'),city_names)))

print("--- list Comprehension----")

output = [city for city in city_names if city.startswith('S')]
print(len(output))
