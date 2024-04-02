import math
def mergeSort(arr):
    merge(arr, 0 ,len(arr) - 1)
    print(arr)

def merge(arr, l, r):
    if (l >= r):
        return
    m = l + math.floor((r-l)/2)
    # if (m == r):
    #     m-=1
    merge(arr, l , m)
    merge(arr, m + 1, r)
    h = arr[l:m+1]
    g = arr[m+1:r+1]
    i = j = 0
    k = l
    while (i!=len(h) and j!= len(g)):
        if (h[i] >= g[j]):
            arr[k] = g[j]
            j+=1
        else:
            arr[k] = h[i]
            i+=1
        k+=1

    if (i!=len(h)):
        arr[k:r+1] = h[i:]
    if (j!=len(g)):
        arr[k:r+1] = g[j:]
arr = [7,6,5,4,3,2,1,0]
mergeSort(arr)

# Time complexity: O(nlogn)
# Space complexity: O(n)

# Notes: 
#      - Do floor always, ceil leads to complications