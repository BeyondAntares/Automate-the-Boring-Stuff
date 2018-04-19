# Cat names
# Have the user enter several cat names, store it into a list and print them.

catNames = [] # Empty List
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '': # If empty string entered, break while loop
        break
    catNames = catNames + [name]  # list concatenation can only concatenate the same data type
print('The cat names are:')
for name in catNames:
    print('  ' + name)
