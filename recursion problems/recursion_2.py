


def fab(n):
    assert n >= 0 and int(n) == n, "The number must be positive and integer number" 
    if(n == 0 or n == 1):
        return 1
    else:
        return fab(n-1) + fab(n-2)


print(fab(1))
