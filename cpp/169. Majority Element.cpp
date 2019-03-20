/*
Source: LeetCode 169. Majority Element
Author: ceezyyy
Date: 03-20-2019
*/


/*
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

*/


#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;

class Solution {
public:
	int majorityElement(vector<int>& nums) {
		map<int, int> majorityCount;
		for (int i = 0; i < nums.size(); i++) {
			majorityCount[nums.at(i)]++;
		}
		for (int j = 0; j < nums.size(); j++) {
			if (majorityCount[nums.at(j)] > nums.size() / 2) {
				return nums.at(j);
			}
		}
		return 0;
	}
};


/*
Submission Detail:

Runtime: 24 ms, faster than 60.88% of C++ online submissions for Majority Element.
Memory Usage: 11.3 MB, less than 50.66% of C++ online submissions for Majority Element.

*/

/*
Study Notes:

Maps are associative containers that store elements in a mapped fashion. 
Each element has a key value and a mapped value. 
No two mapped values can have same key values.

*/