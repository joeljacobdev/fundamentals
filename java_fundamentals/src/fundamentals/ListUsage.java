package fundamentals;

import java.util.*;

public class ListUsage {
    public static void main(String[] args) {
        ArrayList<String> cars = new ArrayList<>();
        cars.add("ferrai");
        cars.add("volvo");
        cars.add("bmw");
        List<String> carList = cars;
        // cast to new String array with size 0
        // understand why Object[] cannot be cast to String[], while Object is parent of String
        String[] carArray = cars.toArray(new String[0]);
        System.out.println(cars + " " + carList + " " + Arrays.toString(carArray));
        Collections.sort(cars, Comparator.reverseOrder());
        Arrays.sort(carArray, (o1, o2) -> o1.charAt(1) - o2.charAt(1));
        System.out.println(cars.get(0) + " " + carList.get(0) + " " + carArray[0]);
        System.out.println(cars.size() + " " + carList.size() + " " + carArray.length);
        // we cannot use primitive types like - char, boolean, double in ArrayList and List - need objects like
        // Character, String


        int[] arr = new int[10];
        arr[0] = 1;
        int[] clonedArr = arr.clone();
        clonedArr[2] = 2;
        // arr prints a reference
        System.out.println(Arrays.toString(clonedArr) + " " + arr);
        int[] threeIntsV1 = new int[]{4, 9, 7};
        int[] threeIntsV2 = {4, 9, 7};
        System.out.println(Arrays.equals(threeIntsV2, threeIntsV1));

        char[] vowels = {'a', 'e', 'i', 'o', 'u'};

        for (char vowel : vowels) {
            System.out.print(vowel);
        }
        System.out.println();
        char[] newArray = Arrays.copyOfRange(vowels, 1, vowels.length);
        for (int i = 0; i < newArray.length; i++) {
            System.out.print(newArray[i]);
        }
        System.out.println();

        int[][] matrix1 = new int[2][3];
        for (int[] row: matrix1) {
            // toIndex is not inclusive
            Arrays.fill(row, 0, 3, -1);
        }
        matrix1[0][0] = 10;
        System.out.println(Arrays.toString(matrix1[0]) + " ++ " + Arrays.toString(matrix1[1]));
        int[][] matrix2 = {
                {1, 2, 3},
                {4, 5, 6}
        };
        System.out.println(Arrays.toString(matrix1) + " " + Arrays.toString(matrix2));

        List<List<Integer>> arrOfArr = new ArrayList<List<Integer>>();
        int size = 10;
        for (int i = 0; i < size; i++) {
            arrOfArr.add(new ArrayList<Integer>());
            arrOfArr.get(i).add(i + 1);
        }
        System.out.println(arrOfArr);
    }
}
