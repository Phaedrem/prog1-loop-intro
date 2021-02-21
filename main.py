# #################
# Name: Darren Bowers
# Coding 04
# Purpose: Program to generate a random number and allow loop on user response.
# #################

# this brings in the random number generator library 
# so we can use it to make random numbers
import random

# these are global constants
# do not use the literals 10 or -10 in your code, use these constants
MIN = -10
MAX = 10

# this is known as a "priming read", so we force our loop to start
choice = "y"

# this begins the loop
while choice == "y":
    # generates a random number -10 to 10 inclusive
    random_num = random.randint(MIN,MAX)
    print("Random Number: ", random_num)

    # write your code here to complete the patterns
    # as shown in the instructions










    # this asks the user to continue
    choice = input("Do you wish to print another pattern (y/n)? ")
