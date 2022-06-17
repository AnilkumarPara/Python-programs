# WAP to read the contents of file and a write 'Python' to end of the file
f=open('Sample.txt',mode='r+')
file_contents=f.read()
print(file_contents)
print("current position=",f.tell())
f.write('\nPython')
f.close()
