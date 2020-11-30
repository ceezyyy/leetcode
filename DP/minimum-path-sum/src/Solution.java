/**
 * Minimum Path Sum
 */
class Solution {

    // 1 <= m, n <= 200
    private int[][] memo = new int[201][201];

    public int minPathSum(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;

        // Base case
        memo[0][0] = grid[0][0];

        // First row
        for (int j = 1; j < cols; j++) {
            memo[0][j] = memo[0][j - 1] + grid[0][j];
        }

        // First col
        for (int i = 1; i < rows; i++) {
            memo[i][0] = memo[i - 1][0] + grid[i][0];
        }

        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                memo[i][j] = Math.min(memo[i - 1][j], memo[i][j - 1]) + grid[i][j];
            }
        }

        return memo[rows - 1][cols - 1];

    }
}