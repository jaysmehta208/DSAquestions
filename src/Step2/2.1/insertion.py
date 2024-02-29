'''
- take every element of unsorted part and insert it into sorted list
- swaps keep happening until right place is found for element in sorted list
'''

def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                break
    print(arr)

insertion([4,8,5,9,1,0])

# Time complexity: O(n^2) Worst case and Average Case
#                  O(n)   Best case                  
