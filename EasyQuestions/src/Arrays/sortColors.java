package Arrays;

import java.util.Arrays;
// Got, after few wrong answers
// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
// color are adjacent, with the colors in the order red, white, and blue.
//
//We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
//
//You must solve this problem without using the library's sort function.
public class sortColors {
    public static void main(String[] args) {
        int[] arr = {1,0};
        sortColors(arr);
        System.out.println(Arrays.toString(arr));
    }
    public static void sortColors(int[] nums) {
        int end0= -1,end1 = -1;
        for (int l = 0; l < nums.length; l++) {
            if (nums[l] ==0) {
                int temp = nums[end0+1];
                nums[end0+1] = 0;
                if (end0!=end1 && end1 < nums.length-1) {
                    int temp2 = nums[end1 + 1];
                    nums[end1 + 1] = temp;
                    if (end1+1!=l) {
                        nums[l] = temp2;
                    }
                } else{
                    nums[l] = temp;
                }
                end0++;
                end1++;

            }
            else if (nums[l] == 1) {
                int temp = nums[end1+1];
                nums[end1+1] = 1;
                nums[l] = temp;
                end1++;
            }
        }
    }
}
