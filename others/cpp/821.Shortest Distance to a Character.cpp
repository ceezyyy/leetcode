/**
 * Source: LeetCode 821. Shortest Distance to a Character
 * Author: ceezyyy
 * Date: 04-16-2019
 */


/*
Easy

Share
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
Input: S = “loveleetcode”, C = ‘e’
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

*/


#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	vector<int> shortestToChar(string S, char C) {
		// initialization
		int len = S.size();
		vector<int> res(len, len);
		int pos = -len;
		// from left -> right
		for (int i = 0; i < len; i++) {
			if (S.at(i) == C) {
				pos = i;
			}
			res.at(i) = min(res.at(i), abs(i - pos));
		}
		// from right -> left
		for (int j = len - 1; j >= 0; j--) {
			if (S.at(j) == C) {
				pos = j;
			}
			res.at(j) = min(res.at(j), abs(j - pos));
		}
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 12 ms, faster than 100.00% of C++ online submissions for Shortest Distance to a Character.
 * Memory Usage: 8.9 MB, less than 100.00% of C++ online submissions for Shortest Distance to a Character.
 */
