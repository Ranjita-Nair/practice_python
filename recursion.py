'''
factorial
    n! = n*(n-1)*....1
    if n =0, return 1
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

fac = factorial(6)
print(fac)
