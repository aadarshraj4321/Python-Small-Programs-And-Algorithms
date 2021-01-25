#import sys
#sys.setrecursionlimit(10000)

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only!"
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)



print(factorial(4))
print(factorial(2))


print()


def factorial_1(num):
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i
        print(fac)



factorial_1(4)
