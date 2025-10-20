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
        user_input = input("Enter the number of terms of the Fibonacci sequence you want: ")  # ask user how many fibonacci terms they want to see, input always comes in as a string
        if user_input.isdigit() and int(user_input) > 0:  # checks that input only has digits and is greater than zero, making sure the number makes sense for a sequence
            return int(user_input)  # converts string to integer once valid so it can be used for loops and math
        print("Please enter a positive integer.")  # gives a clear message when user input isn’t valid so they can fix it
def fibonacci_sequence(terms):
    a, b = 0, 1  # start from the first two numbers of fibonacci, 0 and 1, which build up all the next numbers
    sequence = []  # store all fibonacci numbers in a list so they can be printed together later
    for i in range(terms):  # loops exactly how many times user asked, building the sequence step by step
        sequence.append(a)  # adds the current fibonacci number to the list
        a, b = b, a + b  # updates values where next number becomes the sum of previous two, core logic of fibonacci
    return sequence  # after loop ends, gives back the complete fibonacci list
def display_sequence(sequence):
    print("Fibonacci sequence:")  # prints a small header to make output clear to the user
    print(*sequence)  # prints all numbers from the list with spaces in between, looks clean and readable
def main():
    while True:
        num_terms = user_input()  # gets valid input from the user using the function above
        fib_sequence = fibonacci_sequence(num_terms)  # calls function to create fibonacci numbers based on user’s input
        display_sequence(fib_sequence)  # sends sequence to print function to display on screen
        again = input("Do you want to generate another sequence? (yes/no): ").lower()  # asks user if they want to run program again and makes sure answer is lowercase
        if again != "yes":  # if user does not type yes, program ends gracefully
            print("Goodbye!")  # prints a short goodbye message so user knows program has finished
            break  # exits out of the while loop to stop the program
main()  # starts the main function so everything runs automatically when the program is executed
