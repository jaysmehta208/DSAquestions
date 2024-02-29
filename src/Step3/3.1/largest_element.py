'''
Given an array ‘arr’ of size ‘n’ find the largest element in the array.



Example:

Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
'''

from sys import *
from collections import *
from math import *

def largestElement(arr, n) -> int:
    mini = -maxsize - 1
    for i in arr:
        if i > mini:
            mini = i
    return mini

# Time complexity: O(n)
