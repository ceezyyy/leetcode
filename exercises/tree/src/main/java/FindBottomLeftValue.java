import java.util.ArrayDeque;
import java.util.Deque;

/**
 * <p>
 * 513. Find Bottom Left Tree Value (Medium)
 * https://leetcode.com/problems/find-bottom-left-tree-value/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/3
 */
public class FindBottomLeftValue {

    private int res = 0;

    public int findBottomLeftValue(TreeNode root) {

        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            int n = queue.size();

            for (int i = 0; i < n; i++) {

                TreeNode cur = queue.poll();

                // Keep tracking the left bottom element
                if (i == 0) res = cur.val;

                if (cur.left != null) queue.offer(cur.left);
                if (cur.right != null) queue.offer(cur.right);

            }

        }

        return res;

    }
}
