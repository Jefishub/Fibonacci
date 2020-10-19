"""
Fibonacci Sequence - Enter a number and have the program
generate the Fibonacci sequence to that number or to the Nth number.
"""

""" In Fibonacci sequence you add 2 previous numbers to get the next number
    (n-2) + (n-1) = (n)
    for example -> 1 + 1 = 2 -> 1 + 2 = 3 -> 2 + 3 = 5 ->...
    First 10 fibonacci numbers are: 1,1,2,3,5,8,13,21,34
"""


def fibonacci(nth_number):
    """This function is the Fibonacci sequence. 
       In Fibonacci sequence you add 2 previous integers to gain the 3rd
       The first two numbers are given (1. number = 1, 2. number = 1)
       This function gets a integer as input and prints a list of fibonacci numbers up to nth_number (input)

    Args:
        nth_number (int): Any positive number
    """
    n1 = 1
    n2 = 1
    print("1. number: 1")
    print("2. number: 1")
    for i in range(nth_number-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

        if i < nth_number-3:
            print(f"{i+3}. number: {n3}")

        #This is the last number in given fibonacci sequence. It has been decorated
        else:
            print("*************")
            print(f"{i+3}. number: {n3}")
            print("*************\n")
                

#Main program
def main():

    print("\n***Welcome to Fibonacci calculator***\n")

    #Program loop -> asking for input and showing results. Loops until "0" given
    while True:
        print("The number you give, will be the last number in the Fibonacci sequence.")
        try:
            nth_number = int(input("Please enter a positive number (enter 0 to exit program):"))
        #If any other input than positive integer -> exception -> loop back to asking input again
        except:
            print("\n***Not a valid input. Please try again***\n")
            continue

        
        if nth_number > 2:
            fibonacci(nth_number)

        #Exit -> break out of main program loop
        elif nth_number == 0:
            """exit prompt"""
            print("Thank you for playing")
            print("***exiting***")
            break

        #if 1 or 2 given as nth_number -> no fibonacci() function called 
        #Fibonacci defined as 1. number = 1, 2. number = 1
        elif nth_number == 1:
            print("*************")
            print("1. number: 1")
            print("*************\n")

        elif nth_number == 2:
            print("1. number: 1")
            print("*************")
            print("2. number: 1")
            print("*************\n")



"""MAIN FUNCTION -> starts the game"""
if __name__ == "__main__":
    main()