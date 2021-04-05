import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 653. Two Sum IV - Input is a BST (Easy)
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/3
 */
public class TwoSumBST {

    private List<Integer> res = new ArrayList<>();

    public boolean findTarget(TreeNode root, int k) {

        if (root == null) return false;

        inorder(root);

        int left = 0;
        int right = res.size() - 1;

        /*
          Return true if there exist two elements in the BST
          so, "left < right" instead of "left <= right"
         */
        while (left < right) {

            int cur = res.get(left) + res.get(right);

            if (k == cur) return true;
            if (k < cur) {
                right--;
            } else {
                left++;
            }

        }

        return false;

    }

    public void inorder(TreeNode root) {

        if (root == null) return;

        inorder(root.left);
        res.add(root.val);
        inorder(root.right);

    }
}
