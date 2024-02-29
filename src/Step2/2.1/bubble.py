'''
- compares and swaps every interation of inner loop
'''

def bubble(arr):
    for i in range(0,len(arr) - 1):
        swap = False
        for j in range(0, len(arr) - i - 1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap = True
        if (not swap):
            break

    print(arr)
bubble([1,2,3,4,5,6,7])

# Time complexity: O(n^2)   worst and average case
#                  O(n)     best case (when the optimisation is present) 
