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

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        j = 0
        k = k%len(nums)
        for i in range(len(nums) - k -1, -1,-1):
            if (j>=i):
                break
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j+=1
        j = len(nums) - 1
        for i in range(len(nums) - k, len(nums)):
            if (j<=i):
                break
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j-=1
        j = len(nums) - 1
        for i in range(0,len(nums)):
            if (j<=i):
                return
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j-=1
        
        
        
