package Arrays;

import java.util.Arrays;
// Rotate Array by 1 places
public class leftRotate1Place {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7};
        leftRotate(arr,arr.length);
    }
    public static void leftRotate(int arr[], int n) {
        int rightNumber = arr[n-1];
        for (int i = n-2; i>=0;i--){
            int temp = arr[i];
            arr[i] = rightNumber;
            rightNumber = temp;

        }
        arr[n-1] = rightNumber;
        System.out.println(Arrays.toString(arr));
    }
}
// O(n) : Time Complexity
// O(1) Auxiliary space