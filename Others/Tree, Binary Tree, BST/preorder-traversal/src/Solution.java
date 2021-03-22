import java.util.LinkedList;
import java.util.List;


/**
 * Binary Tree Preorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private List<Integer> result = new LinkedList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        pre(root);
        return result;
    }

    public void pre(TreeNode node) {
        if (node == null) return;
        result.add(node.val);
        pre(node.left);
        pre(node.right);
    }

} 