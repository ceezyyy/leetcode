/**
 * Source: LeetCode  532. K-diff Pairs in an Array
 * Author: ceezyyy
 * Date: 05-09-2019
 * Reference: @fuxuemingzhu https://blog.csdn.net/fuxuemingzhu/article/details/79255633
 */


/*
Easy

Share
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won¡¯t exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

*/


#include<map>
#include<vector>
using namespace std;

class Solution {
public:
	int findPairs(vector<int>& nums, int k) {
		// we need to find the number of unique k-diff pairs in the array
		// so we use map
		int res = 0; // initialize to 0
		map<int, int> m;
		for (int num : nums) {
			m[num]++;
		}
		for (const auto &it : m) {
			if (k == 0 && it.second > 1) {
				res++;
			}
			if (k > 0 && m.count(it.first + k))
				// the count() function 
				// returns the number of elements in the map whose key value is equal to key.
				res++;
		}
		return res;
	}
};


// Study Notes:
// iterator & map


/**
 * Submission Detail:
 * Runtime: 48 ms, faster than 34.44% of C++ online submissions for K-diff Pairs in an Array.
 * Memory Usage: 15.5 MB, less than 10.00% of C++ online submissions for K-diff Pairs in an Array.
 */
