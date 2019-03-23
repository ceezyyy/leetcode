/*
Source: LeetCode 231. Power of Two
Author: ceezyyy
Date: 03-23-2019
*/


/*
Easy

Share
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false

*/


#include<iostream>
#include<math.h>
using namespace std;
class Solution {
public:
	bool isPowerOfTwo(int n) {
		if (n == 1 || n == 2 || n == 4 || n == 8) { return true; }
		for (int i = 0; i <= sqrt(n); i++) {
			if (pow(2, i) == n) {
				return true;
			}
		}
		return false;
	}
};


/*
Submission Detail:

Runtime: 24 ms, faster than 50.20% of C++ online submissions for Power of Two.
Memory Usage: 8.3 MB, less than 5.11% of C++ online submissions for Power of Two.

*/


/*
Study Notes:

My solution sucks... I'm supposed to learn more!!!

*/
