/*
Source: LeetCode 485. Max Consecutive Ones 
Author: ceezyyy
Date: 04-01-2019
*/


/*
Easy

Share
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

*/


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	int findMaxConsecutiveOnes(vector<int>& nums) {
		vector<int> res;
		int tempCount = 0;  /* count the number of consecutive 1s */

		for (int i = 0; i < nums.size(); i++) {
			if (nums.at(i) != 0) {
				tempCount++;
			}
			else {
				res.push_back(tempCount);
				/*
				Each length(number) of consecutive 1s,
				here use vector in order to find the maximum number
				by sorting the array
				*/
				tempCount = 0;
			}
		}
		res.push_back(tempCount);  /* it can return zero even if all elements are zero */
		sort(res.begin(), res.end(), greater<int>());  /* find the maximum number of consecutive 1s */
		return res.at(0);
	}
};


/*
Submission Detail:

Runtime: 44 ms, faster than 21.76% of C++ online submissions for Max Consecutive Ones.
Memory Usage: 12.4 MB, less than 5.07% of C++ online submissions for Max Consecutive Ones.

*/
