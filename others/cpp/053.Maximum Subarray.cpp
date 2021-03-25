/**
 * Source: LeetCode 053. Maximum Subarray
 * Author: ceezyyy
 * Date: 04-10-2019
 */


/*
Easy

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

*/


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		long int res = nums.at(0);
		long int sum = 0;
		for (int i = 0; i < nums.size(); i++) {
			sum = 0;
			for (int j = i; j < nums.size(); j++) {
				sum += nums.at(j);
				if (sum > res) {
					res = sum;
				}
			}
		}
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 304 ms, faster than 5.30% of C++ online submissions for Maximum Subarray.
 * Memory Usage: 9.2 MB, less than 99.75% of C++ online submissions for Maximum Subarray.
 */
