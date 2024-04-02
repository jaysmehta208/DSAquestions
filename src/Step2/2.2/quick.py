from typing import List
def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if (startIndex >= endIndex):
        return
    pivot = arr[endIndex]
    i = -1
    j = startIndex
    while (i!= endIndex and j!= endIndex):
        if (arr[j] > pivot):
            if (i==-1):
                i = j
            j+=1
        else:
            if (i==-1):
                j+=1
                continue
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
            j+=1
    if (i!=-1):
        temp = arr[i]
        arr[i] = pivot
        arr[endIndex] = temp
        quickSort(arr, startIndex, i-1)
        quickSort(arr, i+1, endIndex)
    else:
        i = endIndex - 1
        quickSort(arr, startIndex, i)
    

arr = [4,3,8,4,6,5]
quickSort(arr, 0, len(arr) - 1)
print(arr)

# Time complexity: O(nlogn)
# Space complexity: O(1)

