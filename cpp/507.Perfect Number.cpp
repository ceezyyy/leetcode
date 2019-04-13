/**
 * Source: LeetCode 507. Perfect Number
 * Author: ceezyyy
 * Date: 04-13-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/6636879.html
 */


/*
Easy

Share
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

*/


#include<iostream>
#include<math.h>
using namespace std;

class Solution {
public:
	bool checkPerfectNumber(int num) {
		int sum = 1;
		for (int i = 2; i <= sqrt(num); i++) {
			if (num%i == 0) {
				sum += i;
				if (num / i != i) { // if num/i==0, then num is a complete square number
					sum += num / i;
				}
			}
		}
		// all its positive divisors except itself (when num equals to 1)
		return (num != 1) && (sum == num);
	}
};


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Perfect Number.
 * Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Perfect Number.
 */
