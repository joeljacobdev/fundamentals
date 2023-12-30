package algorithm;

import java.util.Arrays;

public class Quicksort {
    private static void quicksort(int[] arr, int start, int end) {
        if (start < end) {
            int partition = getPartition(arr, start, end);
            quicksort(arr, start, partition - 1);
            quicksort(arr, partition + 1, end);
        }
    }

    private static void swap(int[] arr, int src, int dest) {
        int temp = arr[src];
        arr[src] = arr[dest];
        arr[dest] = temp;
    }

    private static int getPartition(int[] arr, int start, int end) {
        int i = start, j = start;
        while (i < end) {
            if (arr[i] <= arr[end]) {
                swap(arr, i, j);
                j++;
            }
            i++;
        }
        swap(arr, j, end);
        return j;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 23, 6, 2, 6};
        quicksort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }
}
