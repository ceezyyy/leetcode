/*
Source: LeetCode 941. Valid Mountain Array
Author: ceezyyy
Date: 03-31-2019
*/


/*
Easy

Share
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < бн A[i-1] < A[i]
A[i] > A[i+1] > бн > A[B.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000

*/


#include<iostream>
using namespace std;
#include<vector>

class Solution {
public:
	bool validMountainArray(vector<int>& A) {
		/*
		A.length >= 3
		*/
		int i = 0;
		if (A.size() < 3) {
			return false;
		}
		else {
			/*
			Walk up
			*/
			while (i + 1 < A.size() && A.at(i) < A.at(i + 1)) {
				i++;
			}
			if (i == 0 || i == A.size() - 1) {
				/*
				0 < i < A.length - 1
				*/
				return false;
			}
			/*
			Walk down
			*/
			while (i + 1 < A.size() && A.at(i) > A.at(i + 1)) {
				i++;
			}
			return i == A.size() - 1;
		}
	}
};


/*
Submission Detail:

Runtime: 36 ms, faster than 76.44% of C++ online submissions for Valid Mountain Array.
Memory Usage: 10.3 MB, less than 100.00% of C++ online submissions for Valid Mountain Array.

*/


/*
Study Notes:

Walk up & down

*/
