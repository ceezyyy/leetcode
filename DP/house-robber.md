# House Robber

**Example**

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```



**Explained**



**Solution.java**

```java
/**
 * House Robber
 */
class Solution {

    // 0 <= nums.length <= 100
    // memo[i]: the maximum amount we can get before "i"
    private int[] memo = new int[101];

    public int rob(int[] nums) {

        // Corner case
        if (nums.length == 0) return 0;

        // Base case
        // "i-th" house: nums[i - 1]
        memo[0] = 0;
        memo[1] = nums[0];

        for (int i = 2; i <= nums.length; i++) {
            // Two choices: rob or not
            memo[i] = Math.max(memo[i - 2] + nums[i - 1], memo[i - 1]);
        }

        return memo[nums.length];

    }
}
```