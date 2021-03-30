/**
 * <p>
 * 700. Search in a Binary Search Tree (Easy)
 * https://leetcode.com/problems/search-in-a-binary-search-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class SearchBST {
    public TreeNode searchBST(TreeNode root, int val) {

        if (root == null) return null;

        /*
          Preorder traversal
         */
        if (val == root.val) return root;

        if (val < root.val) {
            return searchBST(root.left, val);
        } else {
            return searchBST(root.right, val);
        }

    }
}
