/**
 * <p>
 * 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree (Medium)
 * https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/1
 */
public class GetTargetCopy {

    private int target;
    private TreeNode res;

    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        this.target = target.val;
        preorder(cloned);
        return res;
    }


    public void preorder(TreeNode root) {

        if (root == null) return;

        /*
          The values of the nodes of the tree are unique
         */
        if (root.val == target) {
            res = root;
            return;
        }

        preorder(root.left);
        preorder(root.right);

    }

}
