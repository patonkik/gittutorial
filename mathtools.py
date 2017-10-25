

def isPrime(n):
    '''Returns true if a number n is a prime number'''
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True
def factorial(n):
    '''Returns the factorial of a number'''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def arithmetic(a, difference, n):
    '''Calculates the sum of a arithmetic serie of n elements.
       An arithmetic sequence is of the form: a, a+d, a+2d, a+3d,...
       n is the number of elements in the sequence.'''
    #Get the arithmetic sequence
    sequence = [a+difference*x for x in range(n)]
    #Calculates its sum
    return sum(sequence)
def fib(n):
    ''' Calculates the n value of the fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def geometric(a, ratio, n):
    '''Calculates the sum of a geometric serie of n elements.
       A geometric sequence is of the form: a, a*r, a*r*r, a*r*r*r,...
       n is the number of elements in the sequence.'''
    #Use the sum formula:
    return a*(1-ratio**n)/(1-ratio)
