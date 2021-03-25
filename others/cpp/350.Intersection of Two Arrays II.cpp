/*
Source: LeetCode 350. Intersection of Two Arrays II
Author: ceezyyy
Date: 03-31-2019
Reference: @Grandyang http://www.cnblogs.com/grandyang/p/5533305.html
*/


/*
Easy

Share
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1¡¯s size is small compared to nums2¡¯s size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

*/


#include<iostream>
using namespace std;
#include<vector>
#include<algorithm>

class Solution {
public:
	vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
		vector<int> res;
		/*
		Tips:
		What if the given array is already sorted?
		To Do:
		Sort two arrays
		*/
		sort(nums1.begin(), nums1.end());
		sort(nums2.begin(), nums2.end());
		int i, j;
		/*
		Two pointers ¡®i¡¯ & 'j' point to two arrays
		*/
		for (i = 0, j = 0; i < nums1.size() && j < nums2.size();) {
			if (nums1.at(i) == nums2.at(j)) {
				res.push_back(nums1.at(i));
				/*
				Each element in the result should appear as many times
				as it shows in both arrays
				*/
				i++;
				j++;
			}
			else if (nums1.at(i) < nums2.at(j)) {
				i++;
			}
			else {
				j++;
			}
		}
		return res;
	}
};


/*
Submission Detail:

Runtime: 8 ms, faster than 100.00% of C++ online submissions for Intersection of Two Arrays II.
Memory Usage: 9 MB, less than 83.44% of C++ online submissions for Intersection of Two Arrays II.

*/


/*
Study Notes:

Two Pointers: 'i' & 'j'.

*/
