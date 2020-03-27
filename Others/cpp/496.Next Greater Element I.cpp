/**
 * Source: LeetCode 496. Next Greater Element I 
 * Author: ceezyyy
 * Date: 04-20-2019
 */


/*
Easy

Share
You are given two arrays (without duplicates) nums1 and nums2 where nums1¡¯s elements are subset of nums2. Find all the next greater numbers for nums1¡¯s elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

*/


#include<vector>
#include<map>
using namespace std;

class Solution {
public:
	vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
		map<int, int> location; // record the location of each element of "nums2"
		vector<int> res;
		int i = 0, j = 0, k = 0;
		for (i = 0; i < nums2.size(); i++) {
			location[nums2.at(i)] = i;
		}
		for (j = 0; j < nums1.size(); j++) { // traversing "nums1"
			for (k = location[nums1.at(j)]; k < nums2.size(); k++) {
				if (nums2.at(k) > nums1.at(j)) {
					res.push_back(nums2.at(k)); // the first greater number to its right in nums2
					break; // just the first greater element
				}
			}
			if (k == nums2.size()) {
				res.push_back(-1); // if it does not exist, output -1 for this number
			}
		}
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 12 ms, faster than 98.72% of C++ online submissions for Next Greater Element I.
 * Memory Usage: 9.3 MB, less than 82.58% of C++ online submissions for Next Greater Element I.
 */
