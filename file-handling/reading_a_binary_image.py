fr=open('Shanvi.jpeg','rb')
print(fr)
image=fr.read()
fw=open('Shanvi-copy.jpeg','wb')
fw.write(image)
fw.close()