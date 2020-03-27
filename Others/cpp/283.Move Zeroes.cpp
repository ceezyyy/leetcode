/**
 * Source: LeetCode 283. Move Zeroes
 * Author: ceezyyy
 * Date: 03-26-2019
 */


/*
Easy

Share
Given an array nums, write a function to move all 0¡¯s to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

*/


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	void moveZeroes(vector<int>& nums) {
		int res = 0; //The slow-runner
		for (int i = 0; i < nums.size(); i++) { //The fast-runner
			if (nums.at(i) != 0) {
				nums.at(res++) = nums.at(i);
			}
		}
		while (res < nums.size()) {
			nums.at(res++) = 0;
		}
	}
};


// Study Notes:
// one slow-runner and one fast-runner at the same time


/**
 * Submission Detail:
 * Runtime: 16 ms, faster than 99.47% of C++ online submissions for Move Zeroes.
 * Memory Usage: 9.4 MB, less than 98.83% of C++ online submissions for Move Zeroes.
 */
