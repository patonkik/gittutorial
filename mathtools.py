

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
def fib(n):
    ''' Calculates the n value of the fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)