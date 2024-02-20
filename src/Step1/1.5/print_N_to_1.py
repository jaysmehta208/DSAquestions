# forward tracking
def rec(n):
    if (n == 0):
        return
    else:
        print(n)
        rec(n-1)

# back tracking
def rec2(index, n):
    if (n+1 == index):
        return
    else:
        rec2(index+1,n)
        print(index)

rec2(1,10)