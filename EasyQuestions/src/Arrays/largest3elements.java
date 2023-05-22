package Arrays;

// Given an array with all distinct elements, find the largest three elements


public class largest3elements {
    public static void main(String[] args) {
        int arr[] = {10, 4, 3, 50, 23, 90};
        int first =Integer.MIN_VALUE,second = Integer.MIN_VALUE,third = Integer.MIN_VALUE;
        for (int  i = 0; i < arr.length;i++) {
            if (arr[i] > third) {
                first = second;
                second = third;
                third = arr[i];
                continue;
            }
            if (arr[i] > second && arr[i]!= third) {
                first =  second;
                second = arr[i];
                continue;
            }
            if (arr[i] > first && arr[i]!= second) {
                first = arr[i];
            }
        }
        System.out.println(first + " " + second + " " + third);




    }
// O(n) : Time Complexity
// O(1) Auxiliary space
}