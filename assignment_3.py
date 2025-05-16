#taking input from user
sentence = input ("write a sentence of your choice: ")

#display total number of characters
print(len(sentence))

# #display total number of words
split_sentence = sentence.split(" ")
print(len(split_sentence))

# #display first 3 characters
print(sentence[:4])

#display last three characters
print(sentence[-3:])

#convert sentence to uppercase
print(sentence.upper())

#convert to lowercase
print(sentence.lower())

#replace space to hyphen
print(sentence.replace(" ", "-"))