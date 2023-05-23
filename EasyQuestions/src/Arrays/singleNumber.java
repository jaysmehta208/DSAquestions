package Arrays;

import java.util.HashMap;
// Got
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
//
// You must implement a solution with a linear runtime complexity and use only constant extra space.
public class singleNumber {
    public static void main(String[] args) {
        System.out.println(hash(new int[]{4,1,2,1,2}));
    }
    public static int singleNumber(int[] nums) {
        int xor = nums[0];
        for (int i = 1; i < nums.length;i++) {
            xor = xor ^ nums[i];
        }
        return xor;
    }
    public static int hash(int[] nums) {

        HashMap<Integer,Integer> a =new HashMap<>();
        for (int i = 0; i < nums.length;i++) {
            if (a.containsKey( nums[i])) {
                a.put(nums[i],a.get(nums[i])+1);
            }
            else {
                a.put(nums[i],1);
            }
        }
        for (int i : a.keySet()) {
            if (a.get(i) == 1) {
                return i;
            }
        }
        return -1;
    }
}

// Time complexity : O(n)
// Space complexity : O(1)