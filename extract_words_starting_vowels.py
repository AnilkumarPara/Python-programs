paragraph = ["There was a fox.", "It was brown in color.", "It was seen near that farm sometime back"]
l=['a','e','i','o','u','A','E','I','O','U']
output_l=[]
for sentence in paragraph:
    for word in sentence.split():
        if word[0] in l:
            output_l.append(word)
print(output_l)


output_co=[word for sentence in paragraph for word in sentence.split() if word[0] in l]
print(output_co)
