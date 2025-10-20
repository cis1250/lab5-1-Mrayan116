#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True



def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")  # ask the user to enter a full sentence
        if len(sentence) > 1 and sentence[0].isupper() and sentence[-1] in ".!?":  # checks if it starts with a capital and ends with punctuation
            return sentence  # returns the valid sentence when conditions are met
        print("Invalid sentence. It must start with a capital letter and end with a period, question mark, or exclamation mark.")  # shows error message for invalid input
________________________________________________________________________________________________________________________________________

def calculate_frequencies(sentence):
    sentence_list = sentence.split()  # splits the sentence into individual words and stores them in a list
    words = []  
    counts = []  # list to hold how many times each word appears, list to hold unique words

    for w in sentence_list:  # loops through each word in the list
        w = w.strip(".,!?").lower()  # removes punctuation and converts to lowercase for accurate counting
        if w in words:  # checks if the word already exists in the list,  finds where the word is stored in the list
            index = words.index(w) 
            counts[index] += 1  # increases the count for that specific word
        else:
            words.append(w)  # adds the new word to the words list, starts its count at one since it appeared for the first time, returns both lists so they can be printed later
            counts.append(1)  
    return words, counts 

def print_frequencies(words, frequencies):
    print("\nWord frequencies:")  # prints header for clarity, loops through each index of the words list
    for i in range(len(words)):  
        print(words[i] + ":", frequencies[i])  # prints word followed by how many times it appeared

def main():
    sentence = get_sentence()  # get and validate sentence from the user
    words, frequencies = calculate_frequencies(sentence)  
    print_frequencies(words, frequencies)  # display the results neatly
main()  
