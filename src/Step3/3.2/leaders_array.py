'''
Problem statement
There is an integer array ‘a’ of size ‘n’.
An element is called a Superior Element if it is greater than all the elements present to its right.
You must return an array all Superior Elements in the array ‘a’.

Note:
The last element of the array is always a Superior Element. 

Example
Input: a = [1, 2, 3, 2], n = 4
Output: 2 3

Explanation: 
a[ 2 ] = 3 is greater than a[ 3 ]. Hence it is a Superior Element. 
a[ 3 ] = 2 is the last element. Hence it is a Superior Element.
The final answer is in sorted order.
'''

from typing import *
import sys
def superiorElements(a : List[int]) -> List[int]:
    l = []
    maxx = -sys.maxsize - 1
    for i in range(len(a) - 1, -1, -1):
        if (a[i] > maxx):
            l.append(a[i])
            maxx = a[i]
    l.sort()
    return l

# Time complexity: O(nlogn) because of sorting
# Space complexity: O(n)