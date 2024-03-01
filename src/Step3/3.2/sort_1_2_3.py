'''
Sort Colors:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''

class Solution(object):
    def sortColors(self, nums):
        count0 = 0
        count1 = 0
        for i in nums:
            if i == 0:
                count0+=1
            elif i==1:
                count1+=1
        for i in range(len(nums)):
            if (i < count0):
                nums[i] = 0
            elif (i < count0 + count1):
                nums[i] = 1
            else:
                nums[i] = 2

# Time complexity: O(n)
# 2 pass approach
                
def sortColors2(nums):
        index0 = 0
        index1 = 0
        index2 = 0
        count0 = 0
        count1 = 0
        count2 = 0
        for i in range(0,len(nums)):
            if (nums[i] == 0):
                nums[index0] = 0
                index0+=1
                count0+=1
                if (count1 != 0):
                    nums[index1] = 1
                index1+=1

                if (count2 != 0):
                    nums[index2] = 2
                index2+=1

            elif (nums[i] == 1):
                nums[index1] = 1
                index1+=1
                count1 +=1
                if (count2 != 0):
                    nums[index2] = 2
                index2+=1
            else:
                nums[index2] = 2
                index2+=1
                count2+=1

# Time complexity: O(n)
# 1 pass approach