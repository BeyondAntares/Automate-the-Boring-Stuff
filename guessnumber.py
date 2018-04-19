# Guess the number program
# User has 7 guesses to find the hidden number
# Hints will be provided to guide them to the number

import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20, can you guess the number?')
print('You have 7 tries, good luck')

for guessesTaken in range(1,8):
    print('Guess # %d' % guessesTaken) 
    guess = int(input('Take a guess '))

    if guess < secretNumber:
        print('Your guess is too low, go higher')
    elif guess > secretNumber:
        print('Your guess is too high, go lower')
    elif guess == secretNumber:
        print('Good job! You guessed the correct number in %d guesses' % guessesTaken)
        break
    else:
        print('You\'re out of guesses, I was thinking of %d ' % secretNumber)
        break
        
        
