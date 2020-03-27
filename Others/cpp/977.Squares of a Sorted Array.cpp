/*
Source: LeetCode 977. Squares of a Sorted Array 
Author: ceezyyy
Date: 03-05-2019
*/


/*

977. Squares of a Sorted Array 

Easy

Share
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

*/


#include <functional>
#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector>       // std::vector
using namespace std;

class Solution {
public:
	vector<int> sortedSquares(vector<int>& A) {
		for (int i = 0; i < A.size(); i++) {
			/* first step,square each element */
			A[i] = A[i] * A[i];  
		}
		/* second step, sort them */
		sort(A.begin(), A.end(), less<int>());  
		return A;
	}
};
