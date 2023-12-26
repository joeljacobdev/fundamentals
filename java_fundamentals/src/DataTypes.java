public class DataTypes {
    public static void main(String[] args) {
        String number = "3";
        int digit = number.charAt(0) - '0';
        // string should be a valid number
        digit = Integer.parseInt("232");
        String s = "s232s";
        // Below are not working
        // => ((Character) s.charAt(1)).isDigit() (type casting from primitive to Character is not allowed.)
        // => new Character(s.charAt(1)).isDigit()
        // Only the below is working
        System.out.println(Character.isDigit(s.charAt(1)));
    }
}
