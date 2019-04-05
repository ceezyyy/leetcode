/**
 * Source: LeetCode 674. Longest Continuous Increasing Subsequence
 * Author: ceezyyy
 * Date: 04-05-2019
 */


/**
 * Easy
 * Share
 * Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
 * Example 1:
 * Input: [1,3,5,4,7]
 * Output: 3
 * Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
 * Even though [1,3,5,7] is also an increasing subsequence, it¡¯s not a continuous one where 5 and 7 are separated by 4.
 * Example 2:
 * Input: [2,2,2,2,2]
 * Output: 1
 * Explanation: The longest continuous increasing subsequence is [2], its length is 1.
 * Note: Length of the array will not exceed 10,000.
 */


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	int findLengthOfLCIS(vector<int>& nums) {
		int count = 1; /* Why is "count" initialized to 1? You can simulate it on the draft paper */
		vector<int> recordLength; /* record the length of each continuous increasing subsequence (subarray) */
		if (nums.size() == 0) { return 0; }
		if (nums.size() == 1) { return 1; }
		if (nums.size() == 2) {
			if (nums.at(1) > nums.at(0)) {
				return 2;
			}
			return 1;
		}
		for (int i = 0; i < nums.size() - 1; i++) {
			if (nums.at(i + 1) > nums.at(i)) {
				count++;
			}
			else {
				recordLength.push_back(count);
				count = 1;
			}
		}
		recordLength.push_back(count); /* do not forget to record the last continuous increasing subsequence's length */
		sort(recordLength.begin(), recordLength.end(), greater<int>());
		return recordLength.at(0); /* the length of longest continuous increasing subsequence (subarray) */
	}
};


/**
 * Submission Detail:
 * Runtime: 16 ms, faster than 98.05% of C++ online submissions for Longest Continuous Increasing Subsequence.
 * Memory Usage: 9.8 MB, less than 5.77% of C++ online submissions for Longest Continuous Increasing Subsequence.
 */



