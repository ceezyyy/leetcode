/*
Source: LeetCode 747. Largest Number At Least Twice of Others 
Author: ceezyyy
Date: 03-23-2019
*/


/*
Easy

Share
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice
as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.

Example 1:
Input: nums = [3, 6, 1, 0]
Output : 1
Explanation : 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.The index of value 6 is 1, so we return 1.

Example 2 :
Input : nums = [1, 2, 3, 4]
Output : -1
Explanation : 4 isn¡¯t at least as big as twice the value of 3, so we return -1.

Note :
nums will have a length in the range[1, 50].
Every nums[i] will be an integer in the range[0, 99].

*/


#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	int dominantIndex(vector<int>& nums) {
		/*
		First determine the size of the vector nums
		*/
		if (nums.size() < 2) {
			/*
			nums will have a length in the range [1, 50]
			*/
			return 0;
		}
		else if (nums.size() == 2) {
			/*
			In order to reduce memory consumption
			*/
			if (nums.at(0) >= 2 * nums.at(1)) {
				return 0;
			}
			else if (nums.at(1) >= 2 * nums.at(0)) {
				return 1;
			}
			else {
				return -1;
			}
		}
		else {
			map<int, int>locationOfElement;
			for (int i = 0; i < nums.size(); i++) {
				/*
				Record the location of the original array
				*/
				locationOfElement[nums.at(i)] = i;
			}
			sort(nums.begin(), nums.end(), greater<int>());
			/*
			Sort the array from larger to smaller
			*/
			if (nums.at(0) >= 2 * nums.at(1)) {
				return locationOfElement[nums.at(0)];
			}
		}
		return -1;
	}
};


/*
Submission Detail:

Runtime: 8 ms, faster than 83.60% of C++ online submissions for Largest Number At Least Twice of Others.
Memory Usage: 10.3 MB, less than 5.43% of C++ online submissions for Largest Number At Least Twice of Others.

*/


/*
Study Notes:

1.First determine the size of the vector nums, in order to reduce memory consumption.
2.Test an array with only a single element.

*/
