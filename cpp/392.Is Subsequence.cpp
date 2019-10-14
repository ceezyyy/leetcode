/**
 * Source: LeetCode  392. Is Subsequence
 * Author: ceezyyy
 * Date: 10-14-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/5842033.html
 */


/*
 Easy

 Given a string s and a string t, check if s is subsequence of t.
 You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
 A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

 Example 1:
 s = "abc", t = "ahbgdc"
 Return true.

 Example 2:
 s = "axc", t = "ahbgdc"
 Return false.

 Follow up:
 If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

 Credits:
 Special thanks to @pbrother for adding this problem and creating all test cases.

 */


#include<iostream>
using namespace std;

class Solution {
public:
	int k = 0;
	bool isSubsequence(string s, string t) {
		// t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100)
		// avoid time limitation
		int slow = 0;  // a slow pointer, point to s
		int fast = 0;  // a fast pointer, point to t
		for (fast = 0; (slow < s.size()) && (fast < t.size()); fast++) {
			if (s.at(slow) == t.at(fast)) {
				slow++;
			}
		}
		return slow == s.size();
	}
};


/**
 * Submission Detail:
 * Runtime: 60 ms, faster than 86.14% of C++ online submissions for Is Subsequence.
 * Memory Usage: 16.9 MB, less than 100.00% of C++ online submissions for Is Subsequence.
 */
