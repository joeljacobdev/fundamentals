public class StringUsage {
    public static void main(String[] args) {
        String s1 = "\tHello1\n , world";
        String lowerHello = s1.split(",")[0].trim().toLowerCase();
        int len = lowerHello.length();
        System.out.println(String.format("%s (%s)", lowerHello.substring(0, len - 1), len));

        StringBuilder sb = new StringBuilder(lowerHello);
        sb.setCharAt(1, 'a');
        sb.append(",world");
        int insertAt = sb.indexOf("w");
        sb.insert(insertAt, " ");
        System.out.println("char to delete " + sb.charAt(5));
        sb.deleteCharAt(5);
        // why length() is function for String while for array it is property?
        // reverse is inplace
        System.out.println(sb.reverse().toString() + "--" + sb.substring(0, insertAt));
    }
}
