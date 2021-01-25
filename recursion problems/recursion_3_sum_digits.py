


def sumofDigits(n):
    assert  n >= 0 and int(n) == n, "The number has to be positive number"
    if(n == 0):
        return 0
    else: 
        return int(n%10) + sumofDigits(int(n/10))




print(sumofDigits(253))
#print(sumofDigits(-11))
print(sumofDigits(22222))
