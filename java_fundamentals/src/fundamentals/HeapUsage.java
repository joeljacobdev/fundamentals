package fundamentals;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class HeapUsage {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap = new PriorityQueue<>(Comparator.comparing((item) -> -1 * item));
        System.out.println(maxHeap.peek());
        maxHeap.add(3);
        maxHeap.add(2);
        maxHeap.addAll(Arrays.asList(1, 7, 2));
        System.out.println(maxHeap.peek());
        // Not suggested to use - int primitive as poll return null when size is 0, which cannot be stored in int type
        Integer poppedValue = maxHeap.poll();
        System.out.println(maxHeap.peek() + " -> popped value " + poppedValue);
    }
}
