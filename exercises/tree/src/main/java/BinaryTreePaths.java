import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 257. Binary Tree Paths (Easy)
 * https://leetcode.com/problems/binary-tree-paths/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class BinaryTreePaths {

    private List<String> res = new ArrayList<>();

    public List<String> binaryTreePaths(TreeNode root) {

        if (root == null) return res;
        preorder(root, new StringBuilder());
        return res;

    }

    public void preorder(TreeNode root, StringBuilder sb) {

        if (root == null) return;

        sb.append(root.val);
        if (root.left == null && root.right == null) {
            res.add(sb.toString());
            return;
        }
        sb.append("->");

        preorder(root.left, new StringBuilder(sb));
        preorder(root.right, new StringBuilder(sb));

    }
}
