# Task 1
name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
str_text = f'My name is {name}, I am {age} years old and i am from USA'
str_text2 = str_text.replace("USA", country)
print(str_text2)

# Task 2
text = input("Enter a sentence: ")
my_text = text.replace("blue", "red", 1)
print(my_text)
# print(text.replace("blue", "red", 1))

# Task 3
word = input("Enter a word: ")
sentence = input("Enter a sentence: ")
index = sentence.find(word)
index2 = sentence.count(word)
if word in sentence:
    print(f'The word "{word}" is found at index {index} and it appears {index2} times in this sentences.')
else:
    print(f'The word "{word}" is not found in this sentence')

# Task 4
file_name = input("Enter a file name: ")
if (file_name.endswith(".txt")) and (file_name.startswith("file_")):
    print("The file name is valid.")
else:
    print("The file name is not valid.")

# Task5
words = input("Enter a list of words: ")
now = words.split(",")
my_words = "-".join(now)
print(my_words)
