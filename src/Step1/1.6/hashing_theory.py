def hash(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    print(d)
l = [1,2,5,2,3,6,6,5]

# Storing and fetching Time complexity: 
#    O(1): Average Case
#    O(n) Worst Case

'''
 Hashing Methods:
 - Division Method (Array Hashing): 
   * If only 10 elements are allowed in array, 
   and values to hash are arr = {2, 5, 16, 28, 139}, do arr[i] % 10, and store
   whatever at remainder index.
   * If multiple elements have same remainder, chain it (linked list)
   * If chain is very long, time complexity will be worst case : O(n)


 ''' 
