package Arrays;
// GOT
// Check if Array Is Sorted and Rotated
//Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some
// number of positions (including zero). Otherwise, return false.
//
//There may be duplicates in the original array.
//
//Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.


public class checkSorted {
    public boolean check(int[] nums) {
        boolean flag = true;
        int prev = nums[0];
        int i ;
        for (i = 1; i < nums.length; i++) {
            if (nums[i] < prev) {
                if (!flag) {
                    return false;
                }
                flag = false;
            }
            prev = nums[i];
        }
        if (nums[0] < nums[i-1] && !flag ) {
            return false;
        }
        return true;
    }
}

// O(n) : Time complexity
// O(1) : Space Complexity
// Mistakes
// 1) First time did not account for rotation
