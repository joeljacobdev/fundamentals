import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

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
        Collections.sort(cars, Collections.reverseOrder());
        Arrays.sort(carArray,  (o1, o2) -> o1.charAt(1) - o2.charAt(1));
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
        for (int i = 0; i < vowels.length; i++) {
            System.out.print(vowels[i]);
        }
    }
}
