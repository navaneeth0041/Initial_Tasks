def collatz(number):
    while number>1:
        if number%2 == 0:
            print(number//2)
            number = number//2

        else:
            print((3*number) + 1)
            number = (number*3) + 1

try: 
    n = int(input("Enter a number greater than 1: "))
    collatz(n)
except ValueError:
    print("Check your input again!!")