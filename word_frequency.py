#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False

    if not text[0].isupper():
        return False

    if not re.search(r'[.!?]$', text):
        return False

    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")  # ask the user to enter a full sentence
        if is_sentence(sentence):  # use the is_sentence function to validate
            return sentence  # returns the valid sentence when conditions are met
        print("Invalid sentence. It must start with a capital letter and end with a period, question mark, or exclamation mark.")  # shows error message for invalid input

def calculate_frequencies(sentence):
    sentence_list = sentence.split()  # splits the sentence into individual words and stores them in a list
    words = []  
    counts = []  # list to hold how many times each word appears, list to hold unique words

    for w in sentence_list:  # loops through each word in the list
        w = w.strip(".,!?").lower()  # removes punctuation and converts to lowercase for accurate counting
        if w in words:  # checks if the word already exists in the list, finds where the word is stored in the list
            index = words.index(w)
            counts[index] += 1  # increases the count for that specific word
        else:
            words.append(w)  # adds the new word to the words list, starts its count at one since it appeared for the first time
            counts.append(1)
    return words, counts  # returns both lists so they can be printed later

def print_frequencies(words, frequencies):
    print("\nWord frequencies:")  # prints header for clarity, loops through each index of the words list
    for i in range(len(words)):
        print(words[i] + ":", frequencies[i])  # prints word followed by how many times it appeared

def main():
    sentence = get_sentence()  # get and validate sentence from the user using the proper function
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)  # display the results neatly

main()
