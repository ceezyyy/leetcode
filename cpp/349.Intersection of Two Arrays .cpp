/*
Source: LeetCode 349. Intersection of Two Arrays 
Author: ceezyyy
Date: 03-24-2019
*/


/*
Easy

Share
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

*/


#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;

class Solution {
public:
	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
		map<int, int> occurences;
		vector<int> res;
		for (int i = 0; i < nums1.size(); i++) {
			occurences[nums1.at(i)]++;
		}
		for (int j = 0; j < nums2.size(); j++) {
			if (occurences[nums2.at(j)] != 0) {
				res.push_back(nums2.at(j));
			}
		}
		/*
		1.Each element in the result must be unique.
		2.The result can be in any order.
		*/
		sort(res.begin(), res.end());
		res.erase(unique(res.begin(), res.end()), res.end());
		/*
		use unique() with sort()
		*/
		return res;
	}

};


/*
Submission Detail:

Runtime: 12 ms, faster than 55.30% of C++ online submissions for Intersection of Two Arrays.
Memory Usage: 9.8 MB, less than 13.06% of C++ online submissions for Intersection of Two Arrays.

*/


/*
Study Notes:

1.The iterator returned by unique points to the next position beyond the end of the non-repeating element range.

2.The algorithm does not directly modify the size of the container. If you need to add or remove elements, you must use container operations.

*/
