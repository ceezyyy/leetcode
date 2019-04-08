/**
 * Source: LeetCode 121. Best Time to Buy and Sell Stock
 * Author: ceezyyy
 * Date: 04-08-2019
 * Reference: @Cloudox_ https://blog.csdn.net/Cloudox_/article/details/52668067
 */


/*
Easy

Share
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

*/


//All we need to do is judge the current price:
//First: If you sell at the current price and the profit is higher, then the profit will be saved to “profits”. 
//Second: If the current buy price is lower, save the price to “minPrice” and continue to observe if you can get more profit. 
//If you can, update “profits”, otherwise, keep “profits”.


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		int profits = 0;
		int minPrice;
		if (prices.size()) {
			minPrice = prices.at(0);
			for (int i = 1; i < prices.size(); i++) {
				if (prices.at(i) - minPrice > profits) {
					profits = prices.at(i) - minPrice;
				}
				if (prices.at(i) < minPrice) {
					minPrice = prices.at(i);
				}
			}
			return profits;
		}
		return 0;
	}
};


/**
 * Submission Detail:
 * Runtime: 8 ms, faster than 99.32% of C++ online submissions for Best Time to Buy and Sell Stock.
 * Memory Usage: 9.5 MB, less than 64.88% of C++ online submissions for Best Time to Buy and Sell Stock.
 */

