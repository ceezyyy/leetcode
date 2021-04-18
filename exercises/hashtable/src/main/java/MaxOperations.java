import java.util.HashMap;
import java.util.Map;

/**
 * <p>
 * 1679. K 和数对的最大数目 (Medium)
 * Two Sum 变式
 * https://leetcode-cn.com/problems/max-number-of-k-sum-pairs/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class MaxOperations {

    private int res = 0;
    // <element, occurrence>
    private Map<Integer, Integer> map = new HashMap<>();

    public int maxOperations(int[] nums, int k) {

        for (int i = 0; i < nums.length; i++) {

            int cur = nums[i];
            // 要碰撞的元素
            int target = k - cur;

            // 先查找, 找到就碰撞
            if (map.getOrDefault(target, 0) > 0) {
                // 碰撞, 出现次数 - 1
                map.put(target, map.get(target) - 1);
                res++;
            } else {
                // 找不到就存进 map
                map.put(cur, map.getOrDefault(cur, 0) + 1);
            }

        }

        return res;

    }
}
