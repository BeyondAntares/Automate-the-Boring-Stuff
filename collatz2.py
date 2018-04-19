# Simpler version of collatz, using the yield function
# The mathmatical sequence resolves to 1 by either //2 or x3+1

def collatz(n):
    print(n)
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            yield(n)
            count += 1
        else:
            n = n * 3 + 1
            yield(n)
            count += 1
    print("Series completed in %d iterations" % count)
    return(n)

print("This is The Collatz Sequence")
user = int(input("Enter a number: "))
print(list(collatz(user)))

'''
Yield is logically similar to a return but the function is not
terminated until a defined return or the end of the function
is reached. When the yield statement is executed, the generator
function is suspended and the value of the yield expression is
returned to the caller. Once the caller finishes (and assumably
uses the value that was sent) execution returns to the generator
function right after the yield statement.
'''
