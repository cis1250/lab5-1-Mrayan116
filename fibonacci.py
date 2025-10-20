#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
# Lab 5 - Part 1: Fibonacci Sequence with Functions
# This program calculates and prints the Fibonacci sequence using functions.

#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# Lab 5 - Part 1: Fibonacci Sequence with Functions
# This program calculates and prints the Fibonacci sequence using functions.


#USED MOLSTY THE SAME COMMENTS FROM LAST CODE BECAUSE THE CODE HAD VERY LITTLE CHANGE
def user_input():
    while True:
        user_input_val = input("Enter the number of terms of the Fibonacci sequence you want: ")  # ask the user how many fibonacci numbers they want to see
        if user_input_val.isdigit() and int(user_input_val) > 0:  # checks if input has only digits and is above zero, meaning it’s valid
            return int(user_input_val)  # returns the input converted to an integer once valid
        print("Please enter a positive integer.")  # tells the user the input is wrong and asks them again

def calculate_fibonacci(terms):
    a, b = 0, 1 
    sequence = []  # list to hold all fibonacci numbers in order
    for i in range(terms): 
        sequence.append(a)  # adds the current fibonacci number to the list
        a, b = b, a + b  # calculates next number by adding previous two values
    return sequence  # only returns the list, does not print

def print_fibonacci(sequence):
    print("Fibonacci sequence:")  # prints a label before showing the list

    # added the improvements from lab three using the "end" to add spaces between the characters
    for num in sequence:  # loop through the list of fibonacci numbers
        print(num, end=" ")  # print each number followed by a space, stay on the same line
    print()  # print a new line after the sequence

def main():
    while True:
        num_terms = user_input()  # gets a valid number of terms from the user
        sequence = calculate_fibonacci(num_terms)  # get the fibonacci sequence
        print_fibonacci(sequence)  # print the sequence nicely
        again = input("Do you want to generate another sequence? (yes/no): ").lower()  # asks user if they want to run it again, makes answer lowercase for easy check
        if again != "yes":  # ends loop if user doesn’t type yes
            print("Goodbye!")  # prints goodbye message when program ends
            break  # stops the while loop and exits program
main()
