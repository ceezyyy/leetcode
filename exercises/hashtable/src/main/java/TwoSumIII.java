import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <p>
 * 170. 两数之和 III - 数据结构设计
 * Two Sum 变式
 * https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
class TwoSumIII {

    private List<Integer> nums;
    // <element, occurrence>
    private Map<Integer, Integer> map;


    /**
     * Initialize your data structure here.
     */
    public TwoSumIII() {
        this.nums = new ArrayList<>();
        this.map = new HashMap<>();
    }

    /**
     * Add the number to an internal data structure..
     */
    public void add(int number) {
        nums.add(number);
        map.put(number, map.getOrDefault(number, 0) + 1);
    }

    /**
     * Find if there exists any pair of numbers which sum is equal to the value.
     */
    public boolean find(int value) {
        for (int i = 0; i < nums.size(); i++) {

            int cur = nums.get(i);
            int target = value - cur;

            if (cur == target) {
                // 判断是否成对
                if (map.getOrDefault(cur, 0) >= 2) return true;
            } else {
                if (map.containsKey(target)) return true;
            }

        }
        return false;
    }
}