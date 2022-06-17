import os
fr=open('Sample.txt',mode='r',encoding='utf-8')
print(fr)
file_contents=fr.readlines()
print(file_contents)

fr.close()
#print(fr.closed)


os.remove('Sample.txt')
