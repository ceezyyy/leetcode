/**
 * <p>
 * 993. Cousins in Binary Tree (Easy)
 * https://leetcode.com/problems/cousins-in-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class IsCousins {

    private boolean res;
    private int x;
    private int y;
    private int parentX = -1;
    private int parentY = -1;
    private int depthX = -1;
    private int depthY = -1;


    public boolean isCousins(TreeNode root, int x, int y) {

        this.x = x;
        this.y = y;

        traverse(root, -1, 0);

        return (parentX != parentY) && (depthX == depthY);

    }

    public void traverse(TreeNode root, int parent, int depth) {

        if (root == null) return;

        /*
          Preorder traversal
         */
        if (root.val == x) {
            this.parentX = parent;
            this.depthX = depth;
        }

        if (root.val == y) {
            this.parentY = parent;
            this.depthY = depth;
        }

        traverse(root.left, root.val, depth + 1);
        traverse(root.right, root.val, depth + 1);

    }
}
