package fundamentals;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

public class QueueUsage {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();
        queue.add("a");
        queue.add("b");
        System.out.println(queue);
        System.out.println(queue.peek());
        queue.poll();
        System.out.println(queue);
        Iterator<String> itr = queue.iterator();
        while (itr.hasNext()) {
            String n = itr.next();
            System.out.print(n + "->");
        }
    }
}
