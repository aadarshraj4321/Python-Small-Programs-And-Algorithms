## Sum of Two Digits

class Sum:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b



if __name__== "__main__":
    a,b = map(int,input().split())
    sum_all = Sum(a,b)
    print(sum_all.add())
 
