
def pri_tri(n): 
    for i in range(n):
        print(" " * (n-i-1) + "* " * (i + 1))
        


n = int(input(" : "))
pri_tri(n)



def pri_tri1(n):
    return [print(" " * (n-i-1) + "* " * (i + 1)) for i in range(n)]


n1 = int(input(" : "))
pri_tri(n)
