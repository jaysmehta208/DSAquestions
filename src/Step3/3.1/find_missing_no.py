'''
Missing number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
'''

class Solution(object):
    def missingNumber(self, nums):
        return (len(nums)*(len(nums) + 1)/2) - sum(nums)
    
# Time complexity: O(n)
# Space complexity: O(1)
    
class Solution2(object):
    def missingNumber2(self, nums):
        xor = 0
        for i in range(len(nums)):
            xor = xor^nums[i]^(i+1)
        return xor
    
# Time complexity: O(n)
# Space complexity: O(1)
# xor of two numbers: x^x = 0, 0^x = x
# xor is a bitwise operator and hence is a fast operation
