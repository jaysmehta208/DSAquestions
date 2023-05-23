package Arrays;
// Had to check method
// Time Complexity : O(2n)
// Space Complexity : O(1)

// Given an array arr[] of size N and an integer K, the task is to left rotate the array K indexes
import java.util.Arrays;

public class leftRotateKPlaces {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        rotate(arr,3);
    }
    public static void reverse (int[] arr, int start, int end) {
        for (int i =0; i < (end-start+1)/2;i++) {
            int temp = arr[start + i];
            arr[start + i]=arr[end-i];
            arr[end-i] = temp;
        }
    }
     public static void rotate(int nums[], int k) {
        int n = nums.length;
        k = k%n;
        reverse(nums,0,k-1);
        reverse(nums,k,n-1);
        reverse(nums,0,n-1);

        System.out.println(Arrays.toString(nums));
    }
}
// Mistake
// 1) Thinking we can do it in hops by k from 10 to 7 to 4 to 1 to behind.. and so on if 10 elements and k = 3..
// and then 9 to 6 to 3 to 0 to behind...
// 2) Had to check the method to solve the question
