'''
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                continue
            else:
                temp = nums[i]
                nums[i] = 0
                nums[j] = temp
                j+=1
                
# Time complexity: O(n)
# Space complexity: O(1)
# Optimal operations

# Two pointer approach: One pointer moves slower than the other and does the necessary operation on the data
#                       while the other iterates thorugh all the data