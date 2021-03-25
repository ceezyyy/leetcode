/**
 * Source: LeetCode 268. Missing Number.cpp
 * Author: ceezyyy
 * Date: 03-22-2019
 */


/*
Easy

Share
Given an array containing n distinct numbers taken from 0, 1, 2, ¡­, n, 
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

*/


#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
	int missingNumber(vector<int>& nums) {
		map<int, int> count;
		for (int i = 0; i < nums.size(); i++) {
			count[nums.at(i)]++;
		}
		for (int j = 0; j <= nums.size(); j++) {
			/*
			Here is 'j<=nums.size()'
			because the array containing n distinct numbers
			taken from 0, 1, 2, ..., n
			*/
			if (count[j] == 0) {
				return j;
			}
		}
		return 0;
	}
};


/**
 * Submission Detail:
 * Runtime: 68 ms, faster than 6.36% of C++ online submissions for Missing Number.
 * Memory Usage: 17.5 MB, less than 5.19% of C++ online submissions for Missing Number.
 */
