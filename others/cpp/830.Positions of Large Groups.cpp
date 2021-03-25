/**
 * Source: LeetCode  830. Positions of Large Groups
 * Author: ceezyyy
 * Date: 05-07-2019
 */


/*
Easy

Share
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = ¡°abbxxxxzyy¡± has the groups ¡°a¡±, ¡°bb¡±, ¡°xxxx¡±, ¡°z¡± and ¡°yy¡±.
Call a group large if it has 3 or more characters. We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Example 1:
Input: ¡°abbxxxxzzy¡±
Output: [[3,6]]
Explanation: ¡°xxxx¡± is the single large group with starting 3 and ending positions 6.

Example 2:
Input: ¡°abc¡±
Output: []
Explanation: We have ¡°a¡±,¡°b¡± and ¡°c¡± but no large group.

Example 3:
Input: ¡°abcdddeeeeaabbbcd¡±
Output: [[3,5],[6,9],[12,14]]

Note: 1 <= S.length <= 1000

*/


#include<vector>
#include<string>
using namespace std;

class Solution {
public:
	vector<vector<int>> largeGroupPositions(string S) {
		int i = 0, j = 0; // two pointers (start & end)
		vector<vector<int>> res;
		for (int k = 0; k < S.size();) {
			i = k;
			for (j = i + 1; j < S.size(); j++) {
				if (S.at(j) == S.at(i))
					continue;
				else
					break;
			}
			if (j - i >= 3) { // call a group large if it has 3 or more characters
				res.push_back({ i,j - 1 }); // here is "j-1"
			}
			k = j; // avoid double counting of the same string
		}
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 12 ms, faster than 70.43% of C++ online submissions for Positions of Large Groups.
 * Memory Usage: 9.3 MB, less than 100.00% of C++ online submissions for Positions of Large Groups.
 */
