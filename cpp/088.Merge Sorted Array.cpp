/**
 * Source: LeetCode 88. Merge Sorted Array
 * Author: ceezyyy
 * Date: 03-25-2019
 */


/*
Easy

Share

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

*/


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		for (int i = 0; i < n; i++) {
			nums1.at(m + i) = nums2.at(i);
		}
		sort(nums1.begin(), nums1.end(), less<int>());
	}
};


/**
 * Submission Detail:
 * Runtime: 8 ms, faster than 90.93% of C++ online submissions for Merge Sorted Array.
 * Memory Usage: 9.2 MB, less than 18.22% of C++ online submissions for Merge Sorted Array.
 */
