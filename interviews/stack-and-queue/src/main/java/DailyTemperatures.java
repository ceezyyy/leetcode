import java.util.ArrayDeque;
import java.util.Deque;

/**
 * <p>
 * 739. Daily Temperatures
 * https://leetcode.com/problems/daily-temperatures/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/22
 */
class DailyTemperatures {
    public int[] dailyTemperatures(int[] T) {

        Deque<Integer> decreasingStack = new ArrayDeque<>();
        int[] res = new int[T.length];

        for (int i = 0; i < T.length; i++) {

            int cur = T[i];

            while (!decreasingStack.isEmpty() && T[decreasingStack.peek()] < cur) {
                int index = decreasingStack.pop();
                res[index] = i - index;
            }

            decreasingStack.push(i);

        }

        return res;

    }
}
