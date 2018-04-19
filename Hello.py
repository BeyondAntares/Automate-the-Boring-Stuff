'''
Automate the Boring stuff
First program in Python
- prints to screen
- prints user inputs to screen
- prints user inputs through string calls
'''

print('Hello world!')           # Prints to screen
print('What is your name?')     # ask for their name
myName = input()                # Takes user input

print('It is good to meet you, ' + myName) # prints data type to screen

# nested functions in print call reduces redundant variable use
# Note len returns an integer, to print an integer we use %d
print('The length of your name is: %d' % len(myName))

print('What is your age?')      # ask for their age
myAge = input()                 # Takes an integer input stores as string
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # Typecasting to add value to the integer

mycolour = input("What is your favorite colour? ")

# printing multiple inputs in one sentence
print('Your name is %s, your age is %d, your favorite color is %s' % (myName, int(myAge), mycolour)) 






