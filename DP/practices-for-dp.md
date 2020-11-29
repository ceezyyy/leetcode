# Practices for DP

Table of Contents
-----------------

* [Climbing Stairs](#climbing-stairs)


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