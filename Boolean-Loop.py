# Boolean values in Loops

name = ''
while not name:
    print('Enter your name:')
    name = input()
    # if a blank string is entered, the loop repeats itself
    # Asking the user for a name
    # Only when a non-blank name is entered will we exit the loop
    
print('How many guests will you have ' + name + '?')
numOfGuests = int(input())

if numOfGuests: # i.e. if numOfGuests is a non blank input, else exits
    print(str(numOfGuests) + '! Be sure to have enough room for all your guests.')
print('Done')
