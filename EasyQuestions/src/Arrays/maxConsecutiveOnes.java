package Arrays;
// Got
// Given a binary array nums, return the maximum number of consecutive 1's in the array.
public class maxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCounter = 0;
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {

                counter++;
            }
            if (nums[i] == 0 || i == nums.length-1){
                if (counter > maxCounter) {
                    maxCounter = counter;
                }
                counter = 0;

            }
        }
        return maxCounter;
    }
}
// Time complexity : O(n)
// Space complexity : O(1)