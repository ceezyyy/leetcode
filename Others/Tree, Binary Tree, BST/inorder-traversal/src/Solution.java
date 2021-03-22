import java.util.LinkedList;
import java.util.List;


/**
 * Binary Tree Inorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private List<Integer> result = new LinkedList<>();

    public List<Integer> inorderTraversal(TreeNode root) {
        in(root);
        return result;
    }

    public void in(TreeNode node) {
        if (node == null) return;
        in(node.left);
        result.add(node.val);
        in(node.right);
    }

}
