import java.util.LinkedList;

public class LinkedListUsage {
    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<>();
        ll.add(1);
        ll.add(2);
        ll.add(3);
        ll.addFirst(0);
        ll.addLast(4);
        System.out.println(ll);
        ll.removeLast();
        ll.removeFirst();
        ll.remove((Integer) 1);
        System.out.println(ll);
        System.out.println(ll.getFirst() + " " + ll.getLast() + " " + ll.size());
    }
}
