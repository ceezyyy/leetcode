/*
Source: LeetCode 645. Set Mismatch 
Author: ceezyyy
Date: 03-23-2019
*/


/*
Easy

Share
The set S originally contains numbers from 1 to n. 
But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice and then find the number that is missing. 
Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array¡¯s numbers won¡¯t have any order.

*/


#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
	vector<int> findErrorNums(vector<int>& nums) {
		map<int, int> appearanceOfElement;
		int extraElement, missingElement;
		vector<int> res;
		for (int i = 0; i < nums.size(); i++) {
			appearanceOfElement[nums.at(i)]++;
		}
		for (int j = 1; j <= nums.size(); j++) {
			/*
			The set S originally contains numbers from 1 to n
			*/
			if (appearanceOfElement[j] == 2) {
				extraElement = j;
			}
			if (appearanceOfElement[j] == 0) {
				missingElement = j;
			}
		}
		res.push_back(extraElement);
		res.push_back(missingElement);
		return res;
	}
};


/*
Submission Detail:

Runtime: 136 ms, faster than 6.15% of C++ online submissions for Set Mismatch.
Memory Usage: 22.3 MB, less than 6.56% of C++ online submissions for Set Mismatch.

*/
