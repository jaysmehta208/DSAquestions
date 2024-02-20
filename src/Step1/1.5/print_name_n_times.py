# printing something n times
def rec1(string, n):
    if (n ==0):
        return
    else:
        print(string)
        rec1(string, n-1)
rec1("Hello", 5)

# Time complexity: O(n)
# Auxiliary Stack Space complexity: O(n) 
# There is a stack in which each recursive call is added, 
# and when the function call finally end, it is removed from stack
# too many function calls: Stack Overflow

# Stack space: stores incomplete recursive function calls that are still open

