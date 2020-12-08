
def right_pattern_tri(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()


n = int(input(" : "))
right_pattern_tri(n)


