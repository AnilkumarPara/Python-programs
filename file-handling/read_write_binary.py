# WAP a to read the Binary file and write the same file to Disk
fr=open("D:\Training\Python\Code\File_Handling\class\Shanvi.jpeg",mode='rb')
file_contents=fr.read()
fr.close()

fw=open("D:\Training\Python\Code\File_Handling\class\Shanvi-copy.jpeg",mode='wb')
fw.write(file_contents)
fw.close()
