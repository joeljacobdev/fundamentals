package fundamentals;

import java.util.Scanner;

public class InputUsage {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        int number = sc.nextInt();
        float floatNum = sc.nextFloat();
        // take arr as input
        System.out.println(name + " " + number + " " + floatNum);
        String[] nums = "1 2 3 5".split(" ");
        for (String num : nums) {
            System.out.print(Integer.parseInt(num));
        }
    }
}
