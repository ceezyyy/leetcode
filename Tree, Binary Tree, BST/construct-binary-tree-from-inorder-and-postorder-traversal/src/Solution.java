import java.util.HashMap;
import java.util.Map;

/**
 * Construct Binary Tree from Inorder and Postorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {

        // Corner case
        if (inorder == null || inorder.length == 0 || inorder.length != postorder.length) return null;

        // Duplicates do not exist in the tree
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTree(inorder, postorder, postorder.length - 1, 0, inorder.length - 1, map);

    }


    /**
     * postorder: determine where the root at
     * inorder: determine the left & right interval
     *
     * @param inorder
     * @param postorder
     * @param postIndex
     * @param inStart
     * @param inEnd
     * @param map
     * @return
     */
    public TreeNode buildTree(int[] inorder, int[] postorder,
                              int postIndex,
                              int inStart, int inEnd,
                              Map<Integer, Integer> map) {

        // Corner case
        if (inStart > inEnd || postIndex >= postorder.length || postIndex < 0) return null;

        TreeNode root = new TreeNode(postorder[postIndex]);

        // Dividing line: left root right
        int inIndex = map.get(postorder[postIndex]);
        root.right = buildTree(inorder, postorder, postIndex - 1, inIndex + 1, inEnd, map);
        // (inEnd - inIndex) represents how many nodes in right subtree
        root.left = buildTree(inorder, postorder, postIndex - (inEnd - inIndex) - 1, inStart, inIndex - 1, map);

        return root;

    }
}
