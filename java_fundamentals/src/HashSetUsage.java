import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class HashSetUsage {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 6));
        HashSet<Integer> hs = new HashSet<>(arr);
        hs.add(1);
        hs.add(3);
        hs.add(2);
        hs.add(1);
        System.out.println(hs.contains(3) + " " + hs.size());
        hs.remove(1);
        System.out.println(hs);
    }
}
