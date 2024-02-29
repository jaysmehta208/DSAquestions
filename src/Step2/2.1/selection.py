'''
- compares all values to find minimum
- only swaps minimum to front of list once per outer iteration 
'''
def selection(arr):
    for i in range(0,len(arr)-1):
        mini = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    print(arr)
selection([6,5,4,3,2,1])

# Time complexity: O(n^2)   For best, worst and average case
        