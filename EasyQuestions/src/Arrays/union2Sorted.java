package Arrays;

import java.util.ArrayList;
// Got it
// Union of two arrays can be defined as the common and distinct elements in the two arrays.
// Given two sorted arrays of size n and m respectively, find their union

public class union2Sorted {
    public static ArrayList<Integer> findUnion(int arr1[], int arr2[], int n, int m) {
        int prev = Integer.MIN_VALUE;
        ArrayList<Integer> needed = new ArrayList<>();
        int i =0, j = 0;
        while(true) {
            if (i < n && j < m) {
                if (arr1[i] == prev) {
                    i++;
                    continue;
                }
                if (arr2[j] == prev) {
                    j++;
                    continue;
                }
                if (arr1[i] < arr2[j]) {
                    needed.add(arr1[i]);
                    prev = arr1[i];
                    i++;
                } else {
                    needed.add(arr2[j]);
                    prev = arr2[j];
                    j++;
                }
            } else if (i < n) {
                if (arr1[i] == prev) {
                    i++;
                } else {
                    needed.add(arr1[i]);
                    prev = arr1[i];
                    i++;
                }
            } else if (j < m) {
                if (arr2[j] == prev) {
                    j++;
                } else {
                    needed.add(arr2[j]);
                    prev = arr2[j];
                    j++;
                }
            } else {
                break;
            }
        }
        return needed;
    }
}

// Time complexity : O(m+n)
// Space complexity : O(m+n)