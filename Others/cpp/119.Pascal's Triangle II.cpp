/**
 * Source: LeetCode  119. Pascal's Triangle II
 * Author: ceezyyy
 * Date: 05-12-2019
 */


/*
Easy

Share
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal’s triangle.
Note that the row index starts from 0.
In Pascal’s triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?

*/


#include<vector>
using namespace std;

class Solution {
public:
	vector<int> getRow(int rowIndex) {
		vector<vector<int>> res;
		for (int i = 0; i <= 33; i++) {
			// given a non-negative index k where k ≤ 33
			vector<int> sub(i + 1);
			sub.at(0) = sub.at(i) = 1; // the first & last '1'
			for (int j = 1; j < i; j++) {
				// in Pascal's triangle
				// each number is the sum of the two numbers directly above it
				sub.at(j) = res[i - 1][j - 1] + res[i - 1][j];
			}
			res.push_back(sub);
		}
		return res.at(rowIndex); // return the kth index row of the Pascal's triangle
	}
};


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 98.31% of C++ online submissions for Pascal's Triangle II.
 * Memory Usage: 9 MB, less than 6.16% of C++ online submissions for Pascal's Triangle II.
 */
