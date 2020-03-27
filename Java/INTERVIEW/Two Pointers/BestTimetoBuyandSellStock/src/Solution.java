/**
 * @Topic 121. Best Time to Buy and Sell Stock
 * @Author Yi Cai
 * @Tag
 * @Date 3/27/2020 9:13 AM
 **/


// Approach 1: (Two Pointers)

class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        int slow = 0;  // keep tracking the min price
        for (int fast = 0; fast < prices.length; fast++) {
            if (prices[fast] < prices[slow]) {
                slow = fast;
            }
            result = Math.max(result, prices[fast] - prices[slow]);  // keep tracking the max profit
        }
        return result;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

