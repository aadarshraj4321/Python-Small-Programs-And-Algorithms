def pattern_sqaure(n):
    for i in range(n):
        print((chr(65 + i) + " ") * n)



n = int(input(" : "))
pattern_sqaure(n)

##############################

def pattern_sqaure2(n):
    return [print((chr(65 + i) + " ") * n) for i in range(n)]


n1 = int(input(" : "))
pattern_sqaure(n1)
