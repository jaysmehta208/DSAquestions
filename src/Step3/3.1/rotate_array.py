'''
Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

# O(n) Space Complexity
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        num2 = [0] * len(nums)
        for i in range(0, len(nums)):
            if (i + k < len(nums)):
                num2[i+k] = nums[i]
            else:
                temp = i + k - (len(nums))
                num2[temp] = nums[i]
        for i in range(len(nums)):
            nums[i] = num2[i]
        
