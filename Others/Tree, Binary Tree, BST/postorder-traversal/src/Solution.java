import java.util.LinkedList;
import java.util.List;

/**
 * Binary Tree Postorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private List<Integer> result = new LinkedList<>();

    public List<Integer> postorderTraversal(TreeNode root) {
        post(root);
        return result;
    }

    public void post(TreeNode node) {
        if (node == null) return;
        post(node.left);
        post(node.right);
        result.add(node.val);
    }

}