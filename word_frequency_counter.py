#Write a Python program that takes a list of words as input and counts the frequency of each word 
#using a dictionary. Display the words along with their frequencies in alphabetical order.
#Example Input:
#["apple", "banana", "apple", "orange", "banana", "apple"]



# Input list of words
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Create an empty dictionary to store word frequencies
word_count = {}

# Count the frequency of each word
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

# Sort the dictionary by key (word) and display the result
for i in sorted(word_count):
    print(f"{i}: {word_count[i]}")








