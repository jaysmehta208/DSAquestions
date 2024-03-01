def bubbleSort(arr: list[int], n: int):
    if (n==1):
        return
    for i in range(0,n-1):
        if (arr[i] > arr[i+1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    bubbleSort(arr, n-1)

# Time complexity: O(n^2)