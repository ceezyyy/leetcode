/**
 * Source: LeetCode  258. Add Digits
 * Author: ceezyyy
 * Date: 04-23-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/4741028.html
 */


/*
Easy

Share
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

*/


class Solution {
public:
	int addDigits(int num) {
		while (num / 10 > 0) { // at least two digits
			int sum = 0;
			while (num > 0) {
				sum += num % 10;
				num /= 10;
			}
			num = sum;
		}
		return num;
	}
};


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Add Digits.
 * Memory Usage: 8.1 MB, less than 83.47% of C++ online submissions for Add Digits.
 */
