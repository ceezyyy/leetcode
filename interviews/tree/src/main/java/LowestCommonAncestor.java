/**
 * <p>
 * 236. Lowest Common Ancestor of a Binary Tree (Medium)
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/3
 */
public class LowestCommonAncestor {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        /*
          We allow a node to be a descendant of itself
         */
        if (root == null || root == p || root == q) return root;

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        /*
          Bottom up -> lowest
         */
        if (left != null && right != null) return root;

        /*
          Constraint: p and q will exist in the tree
          So, at least one node is not null
         */
        return left == null ? right : left;

    }

}
