"""
Fibonacci Sequence - Enter a number and have the program
generate the Fibonacci sequence to that number or to the Nth number.
"""

"""fibonacci sequence is Nth number = (n-1)th number + (n-2)th number"""
"""main function"""
def main():
    print("Welcome to Fibonacci calculator")
    while True:
        print("The number you give, will be the Nth number in the Fibonacci sequence.")
        try:
            nth_number = int(input("Please enter a positive number (enter 0 to exit program):"))
        except:
            print("\n***Not a valid input. Please try again***\n")
            continue

        if type(nth_number) == int and nth_number > 2:
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
                else:
                    print("*************")
                    print(f"{i+3}. number: {n3}")
                    print("*************\n")
                    
        
        elif nth_number == 0:
            """exit prompt"""
            print("Thank you for playing")
            print("***exiting***")
            break

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
