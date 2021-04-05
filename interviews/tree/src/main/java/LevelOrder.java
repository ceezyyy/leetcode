import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

/**
 * <p>
 *
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/2
 */
public class LevelOrder {
    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Queue<TreeNode> queue = new ArrayDeque<>();

        if (root == null) return res;

        queue.offer(root);

        /*
          breadth-first search
         */
        while (!queue.isEmpty()) {

            /*
              How many nodes in current layer
             */
            int size = queue.size();
            List<Integer> currentLayer = new ArrayList<>();

            /*
              Walk through current layer
             */
            while (size > 0) {

                TreeNode cur = queue.poll();

                currentLayer.add(cur.val);
                size--;

                if (cur.left != null) queue.offer(cur.left);
                if (cur.right != null) queue.offer(cur.right);

            }

            /*
              We've done, get ready for next layer (if exists)
             */
            res.add(currentLayer);

        }

        return res;

    }
}
