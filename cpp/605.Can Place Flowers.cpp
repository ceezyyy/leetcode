/**
 * Source: LeetCode  605. Can Place Flowers
 * Author: ceezyyy
 * Date: 04-16-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/6983982.html
 */


/*
Easy

Share
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won’t violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won’t exceed the input array size.

*/


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	bool canPlaceFlowers(vector<int>& flowerbed, int n) {
		// traverse
		// consider the previous and next elements of the current element
		for (int i = 0; i < flowerbed.size(); i++) {
			if (n == 0) { return true; }
			if (flowerbed.at(i) == 0) {
				int pre = (i == 0 ? 0 : flowerbed.at(i - 1)); // consider the special case of the beginning
				int next = (i == flowerbed.size() - 1 ? 0 : flowerbed.at(i + 1)); // consider the special case of the end
				if (pre == 0 && next == 0) {
					flowerbed.at(i) = 1;
					n--;
				}
			}
		}
		return n <= 0;
	}
};


/**
 * Submission Detail:
 * Runtime: 20 ms, faster than 91.27% of C++ online submissions for Can Place Flowers.
 * Memory Usage: 10.1 MB, less than 100.00% of C++ online submissions for Can Place Flowers.
 */
