/**
 * Populating Next Right Pointers in Each Node
 */
class Solution {

    public class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;
    }

    public Node connect(Node root) {
        if (root == null) return root;
        connect(root.left, root.right);
        return root;
    }

    public void connect(Node left, Node right) {

        if (left == null || right == null) return;

        left.next = right;
        right.next = null;

        connect(left.left, left.right);
        connect(left.right, right.left);
        connect(right.left, right.right);

    }
}