def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

'''
once and exception is caught, it exits the try loop and goes straight
into the except section. That's why spam(1) is never reached
'''
