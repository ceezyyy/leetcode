/*
Source: LeetCode 509. Fibonacci Number
Author: ceezyyy
Date: 03-11-2019
*/


/*

Easy

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:

0 ¡Ü N ¡Ü 30.

*/


#include<iostream>
using namespace std;

class Solution {
public:
	int fib(int N) {
		if (N == 0) { return 0; }
		if (N == 1) { return 1; }
		else {
			return fib(N - 1) + fib(N - 2);
		}
	}
};


/*

Submission Detail:

Runtime: 16 ms, faster than 27.76% of C++ online submissions for Fibonacci Number.
Memory Usage: 8.3 MB, less than 71.08% of C++ online submissions for Fibonacci Number.

*/
