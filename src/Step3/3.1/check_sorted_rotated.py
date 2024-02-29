'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
'''

class Solution(object):
    def check(self, nums):
        oneAllowed = False
        before = nums[0]
        for i in nums:
            if (i >= before):
                before = i
                continue
            else:
                if (not oneAllowed):
                    oneAllowed = True
                    before = i
                    continue
                else:
                    return False
        if (oneAllowed):
            if (nums[0] < nums[len(nums) - 1] ):
                return False
        return True
            
# Time complexity: O(n)