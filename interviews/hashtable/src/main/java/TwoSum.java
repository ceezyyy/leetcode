import java.util.HashMap;
import java.util.Map;

/**
 * <p>
 * 1. Two Sum
 * https://leetcode.com/problems/two-sum/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/15
 */
class TwoSum {
    public int[] twoSum(int[] nums, int target) {

        int n = nums.length;
        /*
          We need to find element frequently
          so, we use hashtable
          <element, indexOfElement>
         */
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {

            int k = target - nums[i];

            if (map.containsKey(k)) return new int[]{i, map.get(k)};
            map.put(nums[i], i);

        }

        return new int[2];

    }
}
