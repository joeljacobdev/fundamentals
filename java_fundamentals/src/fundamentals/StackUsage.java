package fundamentals;

import java.util.Arrays;
import java.util.Stack;

public class StackUsage {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.pop();
        stack.peek();
        stack.size();
        stack.pop();
        stack.empty();
        stack.addAll(Arrays.asList(1, 33, 5));
        System.out.println(stack);
    }
}
