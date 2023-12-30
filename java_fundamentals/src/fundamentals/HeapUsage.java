package fundamentals;

import java.util.Comparator;
import java.util.PriorityQueue;

public class HeapUsage {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        minHeap.add(3);
        minHeap.add(6);
        minHeap.add(2);
        System.out.println(minHeap.peek());
        // Not suggested to use - int primitive as poll return null when size is 0, which cannot be stored in int type
        Integer poppedValue = minHeap.poll();
        System.out.println(minHeap.peek() + " -> popped value " + poppedValue);
    }
}
