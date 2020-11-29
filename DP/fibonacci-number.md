# Fibonacci Number

**Example**

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
```

Given `N`, calculate `F(N)`

**Explained**

**Solution.java**

```java
/**
 * Fibonacci Number
 */
class Solution {

    // 0 ≤ N ≤ 30
    private int[] dp = new int[31];

    public int fib(int N) {

        // Base case
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[N];

    }
}
```