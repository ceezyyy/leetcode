import java.util.HashMap;
import java.util.Map;

/**
 * Construct Binary Tree from Preorder and Inorder Traversal
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

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        // Corner case
        if (preorder == null || preorder.length == 0 || inorder == null || inorder.length == 0) return null;

        Map<Integer, Integer> map = new HashMap<>();
        // Duplicates do not exist in the tree
        for (int i = 0; i < preorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTree(preorder, inorder, 0, 0, preorder.length - 1, map);

    }

    /**
     * preorder: determine where the root at
     * inorder: determine the left & right interval
     *
     * @param preorder
     * @param inorder
     * @param preIndex
     * @param inStart
     * @param inEnd
     * @param map
     * @return
     */
    public TreeNode buildTree(int[] preorder, int[] inorder,
                              int preIndex,
                              int inStart, int inEnd,
                              Map<Integer, Integer> map) {

        // Corner case
        if (inStart > inEnd || preIndex < 0 || preIndex >= preorder.length) return null;

        TreeNode root = new TreeNode(preorder[preIndex]);

        // Dividing line: left root right
        int inIndex = map.get(preorder[preIndex]);

        root.left = buildTree(preorder, inorder, preIndex + 1, inStart, inIndex - 1, map);
        // (inIndex - inStart) represents how many nodes in left subtree
        root.right = buildTree(preorder, inorder, preIndex + (inIndex - inStart) + 1, inIndex + 1, inEnd, map);

        return root;

    }
}