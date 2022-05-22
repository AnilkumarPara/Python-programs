concept=input('Enter the concept name')
number=int(input('Enter the number'))
# old style
print('--old style--')
print('%s supports in %d languages'%(concept,number))
# format function
print('--format functione--')
print('{concept} supports in {number} languages'.format(concept=concept,number=number))
# f string
print('--f string--')
print(f'{concept} supports in {number} languages')
 

