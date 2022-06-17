# WAP to write the following output to a file
# Final output: Jython is a good programming language
# Step 1: Write 'Python' to a file
# Step 2: Replace Python to Jython
# Step 3: Append 'is a good programming language' to Jython
fw=open('Sample_Program.txt',mode='w')
#print(fw)
fw.write('Python')
print('Current position=',fw.tell())
fw.seek(0,0)
print('Current position after seek=',fw.tell())
fw.write('J')
print('Current position after write=',fw.tell())
fw.close()

fa=open('Sample_Program.txt',mode='a')
fa.write(' is a good programming language')
fa.close()
