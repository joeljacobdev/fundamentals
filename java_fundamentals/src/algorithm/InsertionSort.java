package algorithm;

import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {5, 2, 23, 6, 2, 6};
        insertionSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    private static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int j = i;
            // try to insert ith element at right place
            while (j > 0 && arr[j - 1] > arr[j]) {
                // if the current element is not at right place - according to previous element, swap them
                // hopefully should be sorted now!!
                swap(arr, j - 1, j);
                j--;
            }
        }
    }

    private static void swap(int[] arr, int src, int dest) {
        int temp = arr[src];
        arr[src] = arr[dest];
        arr[dest] = temp;
    }
}
