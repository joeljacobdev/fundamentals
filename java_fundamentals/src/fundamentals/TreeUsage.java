package fundamentals;

import java.util.HashMap;
import java.util.HashSet;

public class TreeUsage {
    private static class Node {
        Node left;
        Node right;
        int val;

        Node(int val) {
            this.val = val;
        }

        Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static void printTree(Node root) {
        if (root == null) {
            return;
        }

        System.out.print(root.val + " ");
        printTree(root.left);
        printTree(root.right);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.right.right = new Node(5);
        root.right.left = new Node(4);
        printTree(root);

    }
}

class AncestorNaryTree {
    private static class Pair<U, V> {
        public final U first;
        public final V second;

        private Pair(U first, V second) {
            this.first = first;
            this.second = second;
        }
    }

    private static class Node {
        int val;
        HashSet<Node> children;

        public Node(int val) {
            this.val = val;
            this.children = new HashSet<>();
        }

        @Override
        public String toString() {
            return "" + val;
        }

        @Override
        public boolean equals(Object other) {
            if (other == null || other.getClass() != getClass()) {
                return false;
            }
            Node node = (Node) other;
            return node.val == val;
        }

        @Override
        public int hashCode() {
            return this.val;
        }
    }

    private static Pair<Node, Boolean> traverse(Node root, int val1, int val2) {
        if (root == null) {
            return null;
        }

        Pair<Node, Boolean> temp = null, result = null;
        for (Node child : root.children) {
            temp = traverse(child, val1, val2);
            if (temp != null && result == null) {
                result = temp;
            } else if (temp != null) {
                return new Pair<>(root, true);
            }
        }

        if (root.val == val1 || root.val == val2) {
            return new Pair<>(root, result != null);
        }
        return result;
    }

    public static void main(String[] args) {
        int[][] treeInput = {
                {1, 2}, {2, 3}, {2, 4}, {2, 5}, {4, 6}, {6, 7}, {6, 9}, {5, 8},
                {11, 12}
        };
        HashMap<Integer, Node> hm = new HashMap<>();
        for (int[] parentChild : treeInput) {
            Node parent = hm.get(parentChild[0]);
            if (parent == null) {
                parent = new Node(parentChild[0]);
                hm.put(parentChild[0], parent);
            }
            Node child = hm.get(parentChild[1]);
            if (child == null) {
                child = new Node(parentChild[1]);
                hm.put(parentChild[1], child);
            }
            parent.children.add(child);
        }

        int[] roots = {1, 11};
        for (int root : roots) {
            Pair<Node, Boolean> ans = traverse(hm.get(root), 7, 4);
            System.out.println(ans != null && ans.second ? ans.first : "-1");
        }
    }
}