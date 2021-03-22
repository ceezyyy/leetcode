import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

/**
 * <p>
 * 496. Next Greater Element I (Easy)
 * https://leetcode.com/problems/next-greater-element-i/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/22
 */
class NextGreaterElement {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        Deque<Integer> stack = new ArrayDeque();

        /**
         * All integers in nums1 and nums2 are unique
         * map <current element, next greater element>
         */
        Map<Integer, Integer> map = new HashMap<>();

        int[] res = new int[nums1.length];

        for (int i = nums2.length - 1; i >= 0; i--) {

            int cur = nums2[i];

            /**
             * Maintaining a decreasing stack
             *
             * for example, you can't see the "short" one behind the "tall" one,
             * what you can see is only the "taller" one (when they are in a line)
             */
            while (!stack.isEmpty() && stack.peek() < cur) {
                stack.pop();
            }

            if (!stack.isEmpty()) map.put(cur, stack.peek());

            stack.push(nums2[i]);

        }

        /**
         * Result
         */
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.getOrDefault(nums1[i], -1);
        }

        return res;

    }
}