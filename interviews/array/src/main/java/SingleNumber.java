import java.util.HashSet;
import java.util.Set;

/**
 * <p>
 * 136. Single Number (Easy)
 * https://leetcode.com/problems/single-number/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class SingleNumber {
    // 解法一: 类似摩尔投票思想, 两两碰撞
//    public int singleNumber(int[] nums) {
//
//        Arrays.sort(nums);
//
//        // Initialization
//        int candidate = nums[0];
//        int cnt = 1;
//
//        for (int i = 1; i < nums.length; i++) {
//            // Change candidate
//            if (cnt == 0) {
//                candidate = nums[i];
//                cnt = 1;
//                continue;
//            }
//            // Offset
//            if (nums[i] == candidate) cnt--;
//        }
//
//        return candidate;
//
//    }

    // 解法二: 2 * (a + b + c) - (a + a + b + b + c) = c
    public int singleNumber(int[] nums) {

        Set<Integer> set = new HashSet<>();
        int sumList = 0;
        int sumSet = 0;

        for (int i = 0; i < nums.length; i++) {
            int cur = nums[i];
            sumList += cur;
            if (!set.contains(cur)) {
                sumSet += cur;
                set.add(cur);
            }
        }

        return 2 * sumSet - sumList;

    }

}

