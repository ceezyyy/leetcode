import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <p>
 * 501. Find Mode in Binary Search Tree (Easy)
 * https://leetcode.com/problems/find-mode-in-binary-search-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/4
 */
public class FindMode {

    private Map<Integer, Integer> map = new HashMap<>();
    private int maxFreq = 0;
    private List<Integer> res = new ArrayList<>();

    public int[] findMode(TreeNode root) {

        preorder(root);

        for (Integer key : map.keySet()) {
            if (map.get(key) == maxFreq) res.add(key);
        }

        // List to int[]
        return res.stream().mapToInt(Integer::intValue).toArray();

    }

    public void preorder(TreeNode root) {

        if (root == null) return;

        int occur = map.getOrDefault(root.val, 0) + 1;
        map.put(root.val, occur);
        maxFreq = Math.max(maxFreq, occur);

        preorder(root.left);
        preorder(root.right);

    }

}
