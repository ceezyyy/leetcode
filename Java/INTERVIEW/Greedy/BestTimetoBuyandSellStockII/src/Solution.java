/**
 * @Topic 122. Best Time to Buy and Sell Stock II
 * @Author Yi Cai
 * @Tag Greedy
 * @Date 3/27/2020 10:41 AM
 **/


class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        // Greedy
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i] < prices[i + 1]) {
                result += prices[i + 1] - prices[i];
            }
        }
        return result;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

