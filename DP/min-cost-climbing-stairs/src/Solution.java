/**
 * Min Cost Climbing Stairs
 */
class Solution {

    // Cost will have a length in the range [2, 1000]
    // Cost[1001] represents the top of the stairs (if cost.length is 1000)
    private int[] memo = new int[1001];

    public int minCostClimbingStairs(int[] cost) {

        int n = cost.length;

        // Base case
        // You can either start from the step with index 0, or the step with index 1
        memo[0] = cost[0];
        memo[1] = cost[1];

        for (int i = 2; i < n; i++) {
            memo[i] = Math.min(memo[i - 2], memo[i - 1]) + cost[i];
        }

        // "n" represents the top of the stairs, we need no cost
        return Math.min(memo[n - 2], memo[n - 1]);

    }
}