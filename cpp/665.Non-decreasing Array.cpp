/**
 * Source: LeetCode  665. Non-decreasing Array
 * Author: ceezyyy
 * Date: 04-28-2019
 * Reference:  @Koala_Tree  https://blog.csdn.net/Koala_Tree/article/details/78337518 
 */


/*
Easy

Share
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can’t get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].

*/


#include<vector>
using namespace std;

class Solution {
public:
	bool checkPossibility(vector<int>& nums) {
		int count = 0; // the amount of the element should be modified
		for (int i = 1; i < nums.size() && count < 2; i++) {
			if (nums.at(i) < nums.at(i - 1)) {
				count++;
				if (i == 1 || nums.at(i - 2) < nums.at(i)) { // e.g: [2,5,3,4]
					nums.at(i - 1) = nums.at(i);
				}
				else {
					nums.at(i) = nums.at(i - 1); // e.g: [4,5,3,7]
				}
			}
		}
		return count < 2;
	}
};


// Study Notes:
// avoid array out of bounds


/**
 * Submission Detail:
 * Runtime: 40 ms, faster than 26.94% of C++ online submissions for Non-decreasing Array.
 * Memory Usage: 10.4 MB, less than 100.00% of C++ online submissions for Non-decreasing Array.
 */
