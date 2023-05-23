package Arrays;

// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
// elements.
//
// Note that you must do this in-place without making a copy of the array.
public class moveZeroes {
    public void moveZeroes(int[] nums) {
        int j = 0;
        for (int i = 0; i < nums.length;i++) {
            if (nums[i]!= 0) {
                nums[j] = nums[i];
                j++;
            }
        }
        for (int i = j; i < nums.length;i++) {
            nums[i] = 0;
        }
    }
}

// Time complexity : O(n+x), x is number of 0s
// Space complexity : O(1)