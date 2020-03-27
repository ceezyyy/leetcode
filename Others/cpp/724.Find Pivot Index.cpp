/**
 * Source: LeetCode 724. Find Pivot Index
 * Author: ceezyyy
 * Date: 04-03-2019
 * Reference: @Huahua https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-724-find-pivot-index/
 */


/**
 * Easy
 * Share
 * Given an array of integers nums, write a method that returns the ¡°pivot¡± index of this array.
 * We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
 * If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
 * Example 1:
 * Input: 
 * nums = [1, 7, 3, 6, 5, 6]
 * Output: 3
 * Explanation:
 * The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
 * Also, 3 is the first index where this occurs.
 * Example 2:
 * Input: 
 * nums = [1, 2, 3]
 * Output: -1
 * Explanation:
 * There is no index that satisfies the conditions in the problem statement.
 * Note:
 * The length of nums will be in the range [0, 10000].
 * Each element nums[i] will be an integer in the range [-1000, 1000].
 */


#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>
using namespace std;

 /**
  * Divide the array into left and right parts, the initial value on the left is 0,
  * the initial value on the right is the sum of all the elements,
  * and the pivot is traversed one by one (to start from zero, otherwise all test data cannot be passed, such as
  * "[-1,-1,-1,0,1,1]"), and update the values of the left and right partial arrays.
  */
class Solution {
public:
	int pivotIndex(vector<int>& nums) {
		if (nums.size()) {
			int l = 0;
			int r = accumulate(nums.begin(), nums.end(), 0);
			for (int i = 0; i < nums.size(); i++) {
				r -= nums.at(i);
				if (l == r) {
					return i;
				}
				l += nums.at(i);
			}
		}
		return -1;
	}
};


/**
 * Submission Detail:
 * Runtime: 28 ms, faster than 98.42% of C++ online submissions for Find Pivot Index.
 * Memory Usage: 9.8 MB, less than 100.00% of C++ online submissions for Find Pivot Index.
 */
