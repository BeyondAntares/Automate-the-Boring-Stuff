# Collatz Sequence

# Function applies collatz rules
def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    else:
        return(3*number + 1)


# Introduction
print("Collatz Sequence, enter a number that will resolve to 1")
print("Even numbers are //2, odd are x3 + 1")

# Variable Defintions
number = int(input("Enter Number: "))
count = 1

#Main loop
while(number != 1):
    number = collatz(number)
    if number == 1:
        print(number, "in %d iterations" % count)
        break
    else:
        print(number)
    count += 1
