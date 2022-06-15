fr=open('Sample.txt',mode='r')
file_contents=fr.readlines()
print(file_contents)

fr.close()
#print(fr.closed)
import os
os.remove('Sample.txt')
