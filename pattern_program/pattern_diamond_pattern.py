
def pattern_diamond(n):
    for i in range(n):
        print(" " * (n-i-1) + "* " *(i+1))
    for i in range(n-1):
        print(" " * (i + 1) + "* " * (n-i-1))


n = int(input(" : "))
pattern_diamond(n)
