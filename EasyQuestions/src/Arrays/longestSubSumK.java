package Arrays;

public class longestSubSumK {
    public static void main(String[] args) {
        int[] arr = {-1, 2, 3};//{1,2,3,1,1,1,1,4,2,3};
        System.out.println( lenOfLongSubarr(arr,arr.length,5));
    }
    public static int lenOfLongSubarr (int A[], int N, int K) {
        int start = 0;
        int maxLength = 0;
        int length = 0;
        int tempSum = 0;
        for (int i = 0; i < N;i++) {
            tempSum+=A[i];
            length++;
            if (tempSum == K) {
                if (maxLength < length) {
                    maxLength = length;
                }
            }
            if (tempSum > K) {
                while(tempSum > K) {
                    tempSum = tempSum - A[start];
                    start++;
                    length--;
                    if (start == i) {
                        break;
                    }
                }
                if (maxLength < length) {
                    maxLength = length;
                }
            }

        }
        return maxLength;
    }
}
