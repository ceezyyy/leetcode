/**
 * Source: LeetCode  1137. N-th Tribonacci Number
 * Author: ceezyyy
 * Date: 10-15-2019
 */


/*
 Easy

 The Tribonacci sequence Tn is defined as follows: 
 T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
 Given n, return the value of Tn.
 
 Example 1:
 
 Input: n = 4
 Output: 4
 Explanation:
 T_3 = 0 + 1 + 1 = 2
 T_4 = 1 + 1 + 2 = 4
 
 Example 2:
 
 Input: n = 25
 Output: 1389537

 Constraints:
 0 <= n <= 37
 The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
 
 */


#include<iostream>
using namespace std;

class Solution {
public:
	// DP
	int tribonacci(int n) {
		if (n == 0)
			return 0;
		if (n == 1 || n == 2)
			return 1;
		vector<int> res(n + 1);  // initialize a vector
		res.at(0) = 0;
		res.at(1) = 1;
		res.at(2) = 1;
		for (int i = 3; i <= n; i++) {
			res.at(i) = res.at(i - 1) + res.at(i - 2) + res.at(i - 3);
		}
		return res.at(n);
	}

};


/**
 * Runtime: 4 ms, faster than 51.04% of C++ online submissions for N-th Tribonacci Number.
 * Memory Usage: 8.5 MB, less than 100.00% of C++ online submissions for N-th Tribonacci Number.
 */
