/**
 * Source: LeetCode 001.Two Sum
 * Author: ceezyyy
 * Date: 03-01-2019
 */

/*
Easy

Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/


#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target)
	{
		vector<int> res;
		for (int i = 0; i < nums.size(); i++)
		{
			int start = nums[i];
			for (int j = i + 1; j < nums.size(); j++)
			{
				if (start + nums[j] == target)
				{
					res.push_back(i);
					res.push_back(j);
				}
			}
		}
		return res;
	}
};
