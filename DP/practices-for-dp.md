# Practices for DP

Table of Contents
-----------------

* [Climbing Stairs](#climbing-stairs)
* [Unique Paths](#unique-paths)



## Climbing Stairs

**Example**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```



**Explained**



**Solution.java**

```java
/**
 * Climbing Stairs
 */
class Solution {

    // 1 <= n <= 45
    // dp[i]: how many ways to climb "i" steps
    private int[] dp = new int[46];

    public int climbStairs(int n) {

        // Base case
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];

    }
}
```

## Unique Paths

**Example**

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

<div align="center"> <img src="robot_maze.png" width="40%"/> </div><br>

**Explained**



**Solution.java**

```java
/**
 * Unique Paths
 */
class Solution {

    // dp[i][j]: Unique paths from dp[0][0] to dp[i][j] 
    private int[][] dp;

    public int uniquePaths(int m, int n) {

        // Corner case
        if (m == 1 || n == 1) return 1;

        dp = new int[m][n];

        // Base case
        dp[0][0] = 0;
        dp[0][1] = 1;
        dp[1][0] = 1;

        // The robot can only move either down or right at any point in time 
        // First row
        for (int j = 2; j < n; j++) dp[0][j] = dp[0][j - 1];
        // First col
        for (int i = 2; i < m; i++) dp[i][0] = dp[i - 1][0];

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];

    }
}
```
