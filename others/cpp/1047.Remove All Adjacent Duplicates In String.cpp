/**
 * Source: LeetCode  1047. Remove All Adjacent Duplicates In String
 * Author: ceezyyy
 * Date: 06-04-2019
 * Reference: @qyx_1995  https://blog.csdn.net/qq_29600137/article/details/90343705
 */


/*
Easy

Share
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

Example 1:
Input: “abbaca”
Output: “ca”
Explanation:
For example, in “abbaca” we could remove “bb” since the letters are adjacent and equal, and this is the only possible move. The result of this move is that the string is “aaca”, of which only “aa” is possible, so the final string is “ca”.

Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.

*/


#include<string>
#include<vector>
using namespace std;

class Solution {
public:
	string removeDuplicates(string S) {
		vector<char> nums;
		for (int i = 0; i < S.size(); i++) { // the pointer go straight ahead
			int len = nums.size();
			// stack
			if (nums.size() != 0 && S[i] == nums.at(len - 1)) {
				nums.pop_back();
			}
			else {
				nums.push_back(S[i]);
			}
		}
		string res = ""; // small 's'
		// return the final string after all such duplicate removals have been made
		for (int j = 0; j < nums.size(); j++) {
			res += nums.at(j);
		}
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 24 ms, faster than 66.63% of C++ online submissions for Remove All Adjacent Duplicates In String.
 * Memory Usage: 13.7 MB, less than 100.00% of C++ online submissions for Remove All Adjacent Duplicates In String.
 */