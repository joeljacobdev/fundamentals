package algorithm;

import java.util.Arrays;

public class SelectionSort {
    private static void swap(int[] arr, int src, int dest) {
        int temp = arr[src];
        arr[src] = arr[dest];
        arr[dest] = temp;
    }

    private static void selectionSort(int[] arr) {
        int n = arr.length;
        int min = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[min] > arr[j]) {
                    min = j;
                }
            }
            swap(arr, i, min);
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 23, 6, 2, 6};
        selectionSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
