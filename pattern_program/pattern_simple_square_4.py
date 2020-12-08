
def pattern_number(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * n)


n = int(input(" : "))
pattern_number(n)



def pattern_number2(n):
    return [print((str(i) + " ") * n) for i in range(1, n + 1)]


n1 = int(input(" : "))
pattern_number2(n1)
