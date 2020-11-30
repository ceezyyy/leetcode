/**
 * N-th Tribonacci Number
 */
class Solution {

    // 0 <= n <= 37
    private int[] memo = new int[38];

    public int tribonacci(int n) {

        // Base case
        memo[0] = 0;
        memo[1] = 1;
        memo[2] = 1;

        for (int i = 3; i <= n; i++) {
            memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1];
        }

        return memo[n];

    }
}