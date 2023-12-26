import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class MathUsage {
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 5, -1, 44, 3};
        List<Integer> arrList = Arrays.stream(arr).boxed().collect(Collectors.toList());
        int maxNum = Collections.max(arrList);
        int minNum = Collections.min(arrList);
        System.out.println(minNum + " " + maxNum);
        // will raise Exception when the array is empty
        maxNum = Arrays.stream(arr).max().getAsInt();
        minNum = Arrays.stream(arr).min().getAsInt();
        System.out.println(minNum + " " + maxNum);

        System.out.println(Math.max(minNum, maxNum));
        System.out.println(Math.min(minNum, maxNum));
        System.out.println(Math.random() * 100);
        System.out.println(Math.pow(minNum, maxNum));
        System.out.println(Math.sqrt(maxNum));
        System.out.println(Math.abs(-1));
        System.out.println(Math.ceil(1.34));
        System.out.println(Math.floor(1.34));
        // floor division - get int directly, no need for casting
        System.out.println(Math.floorDiv(3, 2));
    }
}
