/**
 * Source: LeetCode 122. Best Time to Buy and Sell Stock II 
 * Author: ceezyyy
 * Date: 04-03-2019
 * Reference: @Grandyang http://www.cnblogs.com/grandyang/p/4280803.html
 */


/*
Easy

Share
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

*/


//Because you can buy and sell indefinitely. If the current price is higher than the previous price,
//add the difference to profits, because we can buy it yesterday and sell it today.
//If the price is even higher tomorrow, we can buy it today and throw it tomorrow.
 
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		int profits = 0;
		if (prices.size()) {
			for (int i = 0; i < prices.size() - 1; i++) {
				if (prices.at(i + 1) >= prices.at(i)) {
					profits += prices.at(i + 1) - prices.at(i);
				}
			}
			return profits;
		}
		return 0;
	}
};


/**
 * Submission Detail:
 * Runtime: 8 ms, faster than 99.26% of C++ online submissions for Best Time to Buy and Sell Stock II.
 * Memory Usage: 9.5 MB, less than 46.57% of C++ online submissions for Best Time to Buy and Sell Stock II.
 */
