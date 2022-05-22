language=input('Enter the language name')
concept=input('Enter the concept name')
# old style
print('--old style--')
print('%s supports %s'%(language,concept))
# format function
print('--format functione--')
print('{language} supports {concept}'.format(language=language,concept=concept))
# f string
print('--f string--')
print(f'{language} supports {concept}')


