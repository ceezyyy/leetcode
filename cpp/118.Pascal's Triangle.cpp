/**
 * Source: LeetCode  118. Pascal's Triangle
 * Author: ceezyyy
 * Date: 05-07-2019
 * Reference: @wcxdell https://blog.csdn.net/a2331046/article/details/51538297
 */


/*
Easy

Share
Given a non-negative integer numRows, generate the first numRows of Pascal’s triangle.
In Pascal’s triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]

*/


#include<vector>
using namespace std;

class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> res; // 2D array
		for (int i = 0; i < numRows; i++) {
			vector<int> sub(i + 1); // the length of each subarray is different
			sub[0] = sub[i] = 1; // the first & last '1'
			for (int j = 1; j < i; j++) {
				sub[j] = res[i - 1][j - 1] + res[i - 1][j];
			}
			res.push_back(sub); // join each subarray
		}
		return res;
	}
};


// Study Notes:
// 2D array & subarray 


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Pascal's Triangle.
 * Memory Usage: 9 MB, less than 12.17% of C++ online submissions for Pascal's Triangle.
 */
