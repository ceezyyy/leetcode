/**
 * Source: LeetCode 070. Climbing Stairs
 * Author: ceezyyy
 * Date: 03-29-2019
 */


/*
Easy

Share
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation:
There are two ways to climb to the top.
1 step + 1 step
2 steps

Example 2:
Input: 3
Output: 3
Explanation:
There are three ways to climb to the top.
4. 1 step + 1 step + 1 step
5. 1 step + 2 steps
6. 2 steps + 1 step

*/


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int climbStairs(int n) {
		if (n == 1) {
			return 1;
		}
		vector<int> dp;
		dp.resize(n + 1, 0);
		dp.at(1) = 1;
		dp.at(2) = 2;
		for (int i = 3; i <= n; i++) {
			dp.at(i) = dp.at(i - 1) + dp.at(i - 2);
		}
		return dp.at(n);
	}
};


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Climbing Stairs.
 * Memory Usage: 8.4 MB, less than 68.98% of C++ online submissions for Climbing Stairs.
 */
