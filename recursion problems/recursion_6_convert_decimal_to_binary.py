


def decimal(n):
    assert n >= 0 and int(n) == n, "Number must be positive"
    #assert int(n) == n, "Number must be positive"
    if(n == 0):
        return 0
    else:
        return n%2 + 10 * decimal(int(n/2))



print(decimal(1.2))
