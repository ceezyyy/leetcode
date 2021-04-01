import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 872. Leaf-Similar Trees (Easy)
 * https://leetcode.com/problems/leaf-similar-trees/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class LeafSimilar {

    private List<Integer> nums1 = new ArrayList<>();
    private List<Integer> nums2 = new ArrayList<>();

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {

        inorder(root1, nums1);
        inorder(root2, nums2);

        for (int i = 0; i < Math.min(nums1.size(), nums2.size()); i++) {
            if (nums1.get(i) != nums2.get(i)) return false;
        }

        return nums1.size() == nums2.size();

    }

    public void inorder(TreeNode root, List<Integer> nums) {

        if (root == null) return;

        inorder(root.left, nums);
        if (root.left == null && root.right == null) nums.add(root.val);
        inorder(root.right, nums);

    }
}
