/**
 * Source: LeetCode  1046. Last Stone Weight
 * Author: ceezyyy
 * Date: 06-03-2019
 */


/*
Easy

Share
We have a collection of rocks, each rock has a positive integer weight.
Each turn, we choose the two heaviest rocks and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left. Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that¡¯s the value of last stone.

Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000

*/


#include<vector>
#include<queue>
using namespace std;

class Solution {
public:
	int lastStoneWeight(vector<int>& stones) {
		priority_queue<int, vector<int>, less<int> >q; // max priority queue
		for (int i : stones) {
			q.push(i);
		}
		while (q.size() > 1) {
			// we choose the two heaviest rocks and smash them together
			int first = q.top();
			q.pop();
			int second = q.top();
			q.pop();
			if (first != second) {
				q.push(first - second);
			}
		}
		return q.empty() ? 0 : q.top();
	}
};


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 60.76% of C++ online submissions for Last Stone Weight.
 * Memory Usage: 8.6 MB, less than 100.00% of C++ online submissions for Last Stone Weight.
 */
