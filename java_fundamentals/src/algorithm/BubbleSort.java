package algorithm;

import java.util.Arrays;

public class BubbleSort {
    private static void swap(int[] arr, int src, int dest) {
        int temp = arr[src];
        arr[src] = arr[dest];
        arr[dest] = temp;
    }

    private static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean alreadySorted = true;
            for (int j = 1; j < n - i; j++) {
                if (arr[j - 1] > arr[j]) {
                    // push the larger to the end
                    swap(arr, j - 1, j);
                    alreadySorted = false;
                }
            }
            if (alreadySorted) {
                break;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 23, 6, 2, 6};
        bubbleSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
