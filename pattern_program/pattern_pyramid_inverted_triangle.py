
def pri_tri(n):
    for i in range(n):
        print(" " * i + "* " * (n-i))


n = int(input(" : "))
pri_tri(n)
        

################################################################


def pri_tri_1(n):
    return [print(" " * i + "* " * (n-i)) for i in range(n)]



n1 = int(input(" : "))
pri_tri_1(n1)
