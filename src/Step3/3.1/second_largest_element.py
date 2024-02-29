'''
You have been given an array ‘a’ of ‘n’ unique non-negative integers.



Find the second largest and second smallest element from the array.



Return the two elements (second largest and second smallest) as another array of size 2.



Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
'''

import sys
def getSecondOrderElements(n,  a):
    max1 = -1
    max2 = -1
    mini1 = sys.maxsize
    mini2 = sys.maxsize
    for i in a:
        if i > max1:
            max1 = i
        if i < mini1:
            mini1 = i
    for i in a:
        if i > max2 and i!= max1:
            max2 = i
        if i < mini2 and i!= mini1:
            mini2 = i
    return  [max2, mini2]

# Time complexity: O(n)
