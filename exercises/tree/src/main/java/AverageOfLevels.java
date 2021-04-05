import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * <p>
 * 637. Average of Levels in Binary Tree (Easy)
 * https://leetcode.com/problems/average-of-levels-in-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/3
 */
public class AverageOfLevels {
    public List<Double> averageOfLevels(TreeNode root) {

        List<Double> res = new ArrayList<>();

        if (root == null) return res;

        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            // The size of current layer
            int n = queue.size();
            int tmp = n;
            double sum = 0;

            while (tmp-- > 0) {

                TreeNode cur = queue.poll();
                sum += cur.val;

                if (cur.left != null) queue.offer(cur.left);
                if (cur.right != null) queue.offer(cur.right);

            }

            res.add(sum / n);

        }

        return res;

    }
}
