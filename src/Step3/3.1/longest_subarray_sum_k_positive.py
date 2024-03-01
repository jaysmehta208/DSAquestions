'''
Problem statement
You are given an array 'a' of size 'n' and an integer 'k'.



Find the length of the longest subarray of 'a' whose sum is equal to 'k'.



Example :
Input: ‘n’ = 7 ‘k’ = 3
‘a’ = [1, 2, 3, 1, 1, 1, 1]

Output: 3

Explanation: Subarrays whose sum = ‘3’ are:

[1, 2], [3], [1, 1, 1] and [1, 1, 1]

Here, the length of the longest subarray is 3, which is our final answer.

Expected time complexity :
The expected time complexity is O(n).


Constraints :
1 <= 'n' <= 5 * 10 ^ 6
1 <= 'k' <= 10^18
0 <= 'a[i]' <= 10 ^ 9
'''

def longestSubarrayWithSumK(a: list[int], k: int) -> int:
    sum1 = 0
    count = 0
    index = 0
    count_max = 0
    i = 0
    while(True):
        if (i == len(a)):
            break
        if (sum1 + a[i] <= k):
            sum1 = sum1 + a[i]
            count +=1
            if (count > count_max and sum1 == k):
                count_max = count
            i+=1
        else:
            sum1 = sum1 - a[index]
            if (index == i):
                i+=1
            index+=1
            count -= 1
    return count_max

# Time complexity: O(n)
# Two pointer approach
