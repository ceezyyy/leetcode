/**
 * Source: LeetCode 728. Self Dividing Numbers
 * Author: ceezyyy
 * Date: 04-14-2019
 */


/*
Easy

Share
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.

*/


#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
	vector<int> res;
	bool selfDividing(int n) {
		string s = to_string(n);
		for (char c : s) {
			if (c == '0') { // a self-dividing number is not allowed to contain the digit zero
				return false;
			}
			else {
				if (n % (c - '0') != 0) { // pay attention to (c-'0')
					return false;
				}
			}
		}
		return true;
	}

	vector<int> selfDividingNumbers(int left, int right) {
		for (int i = left; i <= right; i++) {
			if (selfDividing(i)) {
				res.push_back(i);
			}
		}
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 8 ms, faster than 44.18% of C++ online submissions for Self Dividing Numbers.
 * Memory Usage: 8.7 MB, less than 30.83% of C++ online submissions for Self Dividing Numbers.
 */
