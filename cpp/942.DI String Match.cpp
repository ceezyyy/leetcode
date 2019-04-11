/**
 * Source: LeetCode 942. DI String Match
 * Author: ceezyyy
 * Date: 04-11-2019
 */


/*
Easy

Share
Given a string S that only contains ¡°I¡± (increase) or ¡°D¡± (decrease), let N = S.length.
Return any permutation A of [0, 1, ¡­, N] such that for all i = 0, ¡­, N-1:

If S[i] == ¡°I¡±, then A[i] < A[i+1]
If S[i] == ¡°D¡±, then A[i] > A[i+1]

Example 1:
Input: ¡°IDID¡±
Output: [0,4,1,3,2]

Example 2:
Input: ¡°III¡±
Output: [0,1,2,3]

Example 3:
Input: ¡°DDI¡±
Output: [3,2,0,1]

Note:
1 <= S.length <= 10000
S only contains characters ¡°I¡± or ¡°D¡±.

*/


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	vector<int> diStringMatch(string S) {
		vector<int> res;
		int i = 0; // min
		int j = S.size(); // max
		for (char c : S) {
			if (c == 'D') { // decrease
				res.push_back(j--);
			}
			else { // increase
				res.push_back(i++);
			}
		}
		res.push_back(i); // the last element
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 40 ms, faster than 99.76% of C++ online submissions for DI String Match.
 * Memory Usage: 10.3 MB, less than 98.79% of C++ online submissions for DI String Match.
 */

