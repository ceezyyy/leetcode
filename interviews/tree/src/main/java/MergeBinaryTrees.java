/**
 * <p>
 * 617. Merge Two Binary Trees (Easy)
 * https://leetcode.com/problems/merge-two-binary-trees/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/29
 */
public class MergeBinaryTrees {
    public TreeNode mergeTrees(TreeNode r1, TreeNode r2) {

        if (r1 == null && r2 == null) return null;

        /*
          When we decide to choose a non-empty element
          between a and b, we can just add them together ("a + b"), because
          the empty one is zero
         */
        int val = (r1 == null ? 0 : r1.val) + (r2 == null ? 0 : r2.val);
        TreeNode newNode = new TreeNode(val);

        /*
          When we do not know whether the node is empty or not
          we can use ternary conditional operator
         */
        newNode.left = mergeTrees(r1 == null ? null : r1.left, r2 == null ? null : r2.left);
        newNode.right = mergeTrees(r1 == null ? null : r1.right, r2 == null ? null : r2.right);

        return newNode;

    }
}


/**
 * References:
 * https://leetcode.com/problems/merge-two-binary-trees/discuss/104299/Java-Solution-6-lines-Tree-Traversal
 */
