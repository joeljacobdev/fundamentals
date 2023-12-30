package fundamentals;

import java.util.HashMap;

public class HashMapUsage {
    public static void main(String[] args) {
        HashMap<String, Integer> hm = new HashMap<>();
        hm.put("Asia", 1);
        hm.put("USA", 2);
        hm.put("Australia", 4);
        hm.put("USA", 3);
        hm.getOrDefault("XYZ", 6);
        System.out.println(hm.get("Japan") + " - " + hm.get("USA"));
        System.out.println(hm.size() + " - " + hm.containsKey("Japan") + " " + hm.containsValue(4));
        hm.remove("Australia");
        System.out.println(hm);
        for (String key : hm.keySet()) {
            System.out.println(key);
        }
        for (Integer value : hm.values()) {
            System.out.println(value);
        }
        hm.clear();
    }
}
