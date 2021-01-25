


def powerofNumber(base, expo):
    #assert (base >= 0 and expo >= 0) and (int(base) == base and int(expo) == expo), "Should be positive"
    assert expo >= 0 and int(exp) == exp, "the exponent must be positive integer only"
    if(expo == 0):
        return 1
    if(expo == 1):
        return base
    return base * powerofNumber(base, expo - 1)



print(powerofNumber(2, -3))
