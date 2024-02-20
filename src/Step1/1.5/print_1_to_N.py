# forward tracking
# doing the task before the next function call
def rec(index,n):
    if (index == n+1):
        return
    else :
        print(index)
        rec(index+1, n)
        
# backtracking
# doing the task after the function call
def rec2(n):
    if (n == 0):
        return
    else:
        rec2(n-1)
        print(n)

rec2(10)