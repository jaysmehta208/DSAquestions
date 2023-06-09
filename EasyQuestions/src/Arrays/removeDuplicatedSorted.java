package Arrays;
import java.util.Arrays;
// GOT

//Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
// element appears only once. The relative order of the elements should be kept the same. Then return the number of
// unique elements in nums.
//
//Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
//
//Change the array nums such that the first k elements of nums contain the unique elements in the order they were
// present in nums initially. The remaining elements of nums are not important as well as the size of nums.
//Return k

public class removeDuplicatedSorted {
    public static int removeDuplicates(int[] nums) {
        int counter = 1;
        int prevNumber  = nums[0];
        int j = 1;
        for (int i = 1; i < nums.length;i++) {
            if (prevNumber == nums[i]) {
                continue;
            }
            counter++;
            prevNumber = nums[i];
            nums[j] = nums[i];
            j++;
        }
        return counter;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,2};
        System.out.println(removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }
}

// Two-pointer approach
// O(n) : Time complexity
// O(1) : Space Complexity