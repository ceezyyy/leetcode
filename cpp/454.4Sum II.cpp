/*
Source: LeetCode 454. 4Sum II
Author: ceezyyy
Date: 03-17-2019
*/


/*
Medium

Share
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ¡Ü N ¡Ü 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2

Explanation:
The two tuples are:
(0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
(1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

*/


#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
	int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
		int count = 0;
		map<int, int> mAB;
		for (int i = 0; i < A.size(); i++) {
			for (int j = 0; j < B.size(); j++) {
				mAB[A.at(i) + B.at(j)++];
				/*
				If an insertion is performed, the mapped value is value-initialized 
				(default-constructed for class types, zero-initialized otherwise) 
				and a reference to it is returned.
				*/
			}
		}
		for (int k = 0; k < C.size(); k++) {
			for (int l = 0; l < D.size(); l++) {
				if (mAB.find(-(C.at(k) + D.at(l))) != mAB.end()) {
					count += mAB[-(C.at(k) + D.at(l))];
				}
			}
		}
		return count;
	}
};

/*
Submission Detail:

Runtime: 388 ms, faster than 21.76% of C++ online submissions for 4Sum II.
Memory Usage: 29.3 MB, less than 69.96% of C++ online submissions for 4Sum II.

*/
