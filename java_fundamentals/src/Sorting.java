import java.time.LocalDate;
import java.util.*;

public class Sorting {
    private static class Coupon {
        int code;
        LocalDate validity;

        Coupon(int code, LocalDate validity) {
            this.code = code;
            this.validity = validity;
        }

        @Override
        public String toString() {
            return this.code + " " + this.validity;
        }
    }
    public static void main(String[] args) {
        LocalDate curr = LocalDate.now();
        List<Coupon> coupons = Arrays.asList(
                new Coupon(10, curr.plusDays(2)),
                new Coupon(15, curr.plusDays(1)),
                new Coupon(-15, curr.plusDays(3))
        );
        coupons.sort((o1, o2) -> o1.validity.compareTo(o2.validity));
        System.out.println(coupons);
        // o1 compareTo o2 => ascending
        // o2 compareTo o1 => descending
        // compareTo only present with Object, not primitive
        Collections.sort(coupons, (o1, o2) -> o1.code - o2.code);
        System.out.println(coupons);
    }
}
