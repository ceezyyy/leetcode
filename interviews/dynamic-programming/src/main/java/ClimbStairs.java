/**
 * <p>
 * 70. Climbing Stairs (Easy)
 * https://leetcode.com/problems/climbing-stairs/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class ClimbStairs {
    public int climbStairs(int n) {

        // Corner case
        if (n == 1) return 1;

        int[] dp = new int[n + 1];
        // One step
        dp[1] = 1;
        // Two steps
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // N steps
        return dp[n];

    }
}
