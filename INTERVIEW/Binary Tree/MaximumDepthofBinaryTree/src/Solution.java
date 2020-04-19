/**
 * @Topic 104. Maximum Depth of Binary Tree
 * @Author Yi Cai
 * @Tag Binary Tree
 * @Date 4/8/2020 10:06 AM
 **/


class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        // left pointer
        int left = maxDepth(root.left);

        //right pointer
        int right = maxDepth(root.right);

        return Math.max(left, right) + 1;
    }
}




