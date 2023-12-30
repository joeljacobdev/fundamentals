package fundamentals;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class DateUsage {
    public static void main(String[] args) {
        LocalDate curr = LocalDate.now();
        LocalDate afterDate = LocalDate.now().plusDays(10);
        LocalDate beforeDate = LocalDate.now().minusDays(10);
        System.out.println(curr.equals(LocalDate.now()));
        System.out.println(afterDate.isAfter(curr));
        System.out.println(beforeDate.isBefore(curr));

        LocalDateTime currTime = LocalDateTime.now();
        LocalDateTime beforeTime = currTime.minusDays(3);
        LocalDateTime afterTime = currTime.plusDays(3);
        System.out.println(currTime.equals(LocalDateTime.now()));
        System.out.println(beforeTime.isBefore(currTime));
        System.out.println(afterTime.isAfter(currTime));
    }
}
