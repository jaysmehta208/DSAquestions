def rec(arr, n):
    if (n == len(arr)):
        return
    temp = arr[n]
    for i in range(n-1,-1,-1):
        if (arr[i] > temp):
            temp1 = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp1
        else:
            arr[i+1] = temp
            break
    rec(arr, n+1)
arr = [6,4,9,2,10,1]
rec(arr, 0)
print(arr)

# Time complexity: O(n)