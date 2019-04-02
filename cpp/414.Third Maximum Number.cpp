/*
Source: LeetCode 414. Third Maximum Number
Author: ceezyyy
Date: 04-02-2019
*/


/*
Easy

Share
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

*/


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

/*
	When I first saw "third", I thought of using array sorting to solve the problem. What's more,
the third maximum here means the third maximum distinct number, that reminds me of the "unique()" function of vector.
	Last but not least, you need to judge the length of the array, avoid crossing the boundary,
and output the results that meet the criteria.
*/

class Solution {
public:
	int thirdMax(vector<int>& nums) {
		sort(nums.begin(), nums.end(), greater<int>());
		nums.erase(unique(nums.begin(), nums.end()), nums.end());
		if (nums.size() == 1) {
			return nums.at(0);
		}
		if (nums.size() == 2) {
			return max(nums.at(0), nums.at(1));
			/*
			the third maximum does not exist, so the maximum (2) is returned instead
			*/
		}
		else {
			return nums.at(2);
		}
	}
};


/*
Submission Detail:

Runtime: 8 ms, faster than 98.80% of C++ online submissions for Third Maximum Number.
Memory Usage: 9.2 MB, less than 69.35% of C++ online submissions for Third Maximum Number.

*/
