package algorithm;

import java.util.Arrays;

public class Mergesort {
    private static int[] mergeSort(int[] arr, int start, int end) {
        if (start == end) {
            return new int[]{arr[start]};
        } else if (start > end) {
            return new int[0];
        }
        int mid = start + Math.floorDiv(end - start, 2);
        int[] leftArr = mergeSort(arr, start, mid);
        int[] rightArr = mergeSort(arr, mid + 1, end);
        return merge(leftArr, rightArr);
    }

    private static int[] merge(int[] leftArr, int[] rightArr) {
        int n = leftArr.length + rightArr.length;
        int[] arr = new int[n];
        int i = 0, j = 0, k = 0;
        while (i < leftArr.length || j < rightArr.length) {
            if (i < leftArr.length && j < rightArr.length) {
                if (leftArr[i] < rightArr[j]) {
                    arr[k] = leftArr[i];
                    i++;
                } else {
                    arr[k] = rightArr[j];
                    j++;
                }
            } else if (i == leftArr.length) {
                arr[k] = rightArr[j];
                j++;
            } else {
                arr[k] = leftArr[i];
                i++;
            }
            k++;
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 23, 6, 2, 6};
        System.out.println(Arrays.toString(mergeSort(arr, 0, arr.length - 1)));
    }
}
