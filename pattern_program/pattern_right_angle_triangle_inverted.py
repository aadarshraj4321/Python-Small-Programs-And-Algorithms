

def right_pattern_tri(n):
    for i in range(n):
        print("* " * (n-i))

n = int(input(" : "))
right_pattern_tri(n)



def right_pattern_tri_1(n):
    return [print("* " * (n - i)) for i in range(n)]


n1 = int(input(" : "))
right_pattern_tri(n1)




def right_pattern_tri2(n):
    for i in range(n + 1):
        for j in range(n-i-1 + 1):
            print("*", end=" ")
        print()



n1 = int(input(" : "))
right_pattern_tri2(n1)


