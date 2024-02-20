def fib(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    return fib(n-1) + fib(n-2)
print(fib(8))

# 0 1 1 2 3 5 8 13

# Time complexity: 2^n