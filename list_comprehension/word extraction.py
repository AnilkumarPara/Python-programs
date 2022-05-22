# WAP to extract each word from a sentence and store all the words in the form of list
paragraph = ["There was a fox." , 'It was brown in color.', "It was seen near that farm sometime back"]

print("---using for loop---")
words=[]
for sentence in paragraph:
    for word in sentence.split():
        words.append(word)
print(words)

print("---using List Comprehension---")
word_s=[word for sentence in paragraph for word in sentence.split()]
print(word_s)
