# parameterised way
# carry changes in the parameters
def rec(sum, index, n):
    if (index == n+1):
        print(sum)
    sum+= index
    rec(sum, index+1, n)

# functional way
# need the recursive function to return something instead of printing
def rec2(n):
    if (n == 0):
        return 0
    return n + rec2(n-1)


print(rec2(10))