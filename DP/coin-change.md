# Coin Change

**Example**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Explained**



**Solution.java**

```java
/**
 * Coin Change
 */
class Solution {

    // 0 <= amount <= 10^4
    // dp[i]: the fewest number of coins to make up "i"
    private int[] dp = new int[10001];

    public int coinChange(int[] coins, int amount) {

        // Base case
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            // Choices
            for (int choice : coins) {
                if (i - choice < 0) continue;
                // Optimal sub-problems
                dp[i] = Math.min(dp[i - choice] + 1, dp[i]);
            }
        }

        return dp[amount] == amount + 1 ? -1 : dp[amount];

    }
}
```