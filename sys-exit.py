# Importing sys and using sys.exit() to exit a program early
# We also have an infinite loop that will only break if the word 'exit' is typed

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
