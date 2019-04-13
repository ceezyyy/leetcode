/**
 * Source: LeetCode 009. Palindrome Number
 * Author: ceezyyy
 * Date: 04-12-2019
 */


/*
Easy

Share
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?

*/


#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

class Solution {
public:
	bool isPalindrome(int x) {
		string res;
		if (x < 0) { return false; }
		else {
			res = to_string(x);
			int i = 0;
			int j = res.size() - 1;
			while (i < j) {
				if (res.at(i++) != res.at(j--)) {
					return false;
				}
			}
		}
		return true;
	}
};


// Study Notes:
// Here convert the integer to a string (Obviously it's not a good idea).


/**
 * Submission Detail:
 * Runtime: 32 ms, faster than 99.61% of C++ online submissions for Palindrome Number.
 * Memory Usage: 8 MB, less than 99.78% of C++ online submissions for Palindrome Number.
 */
