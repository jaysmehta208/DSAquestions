package Arrays;
// Got, Has a BETTER APPROACH
// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
// that is missing from the array
public class missingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for (int i = 0; i < n;i++) {
            sum+=nums[i];
        }
        return ((n+1)*n/2 - sum);

    }
}

// Time complexity : O(n)
// Space complexity : O(1)
// BEST APPROACH : Use XOR, XOR of two identical numbers is 0
// One array XOR1 of all natural numbers till N
// Other array XOR2 of all numbers in array of size N-1
// XOR1 ^ XOR2 gives answer
