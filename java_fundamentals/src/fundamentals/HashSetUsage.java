package fundamentals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class HashSetUsage {

    private static class Coupon {
        int code;

        Coupon(int code) {
            this.code = code;
        }

        @Override
        public String toString() {
            return this.code + "";
        }

        @Override
        public int hashCode() {
            return this.code;
        }

        @Override
        public boolean equals(Object other) {
            if (other == null || getClass() != other.getClass()) {
                return false;
            }
            Coupon cat = (Coupon) other;
            return cat.code == code;
        }
    }

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
        hs.clear();

        HashSet<Coupon> hashObjs = new HashSet<>();
        hashObjs.addAll(Arrays.asList(
                new Coupon(1), new Coupon(2), new Coupon(3), new Coupon(2)
        ));
        System.out.println(hashObjs);
    }
}
