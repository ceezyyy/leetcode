/**
 * Source: LeetCode 136. Single Number 
 * Author: ceezyyy
 * Date: 03-21-2019
 */


/*
Easy

Share
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

*/


#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
	int singleNumber(vector<int>& nums) {
		map<int, int> numAppearance;
		for (int i = 0; i < nums.size(); i++) {
			numAppearance[nums.at(i)]++;
		}
		for (int j = 0; j < nums.size(); j++) {
			if (numAppearance[nums.at(j)] == 1) { //Find that single one
				return nums.at(j);
			}
		}
		return 0;
	}
};


/**
 * Submission Detail:
 * Runtime: 32 ms, faster than 11.83% of C++ online submissions for Single Number.
 * Memory Usage: 11.7 MB, less than 5.09% of C++ online submissions for Single Number.
 */
