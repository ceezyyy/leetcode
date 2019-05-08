/**
 * Source: LeetCode  066. Plus One
 * Author: ceezyyy
 * Date: 03-17-2019
 */


/*
Easy

Share
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

*/


#include<vector>
using namespace std;

class Solution {
public:
	vector<int> plusOne(vector<int>& digits) {
		int carry = 1;
		for (int i = digits.size() - 1; i >= 0; i--) {
			digits.at(i) += carry;
			if (digits.at(i) > 9) { // the same as 'if(digits.at(i)>=10)' 
				digits.at(i) -= 10;
				carry = 1;
			}
			else {
				// if the above is true, you can set the value of carry to 0 and then break directly
				carry = 0;
				break;
			}
		}
		if (digits.at(0) == 0) {
			// judge whether the starting position is 0 or not.
			digits.insert(digits.begin(), 1);
		}
		return digits;
	}
};


// Study Notes:
// consider the problem from a simple situation, and get a good command of the usage of STL


/**
 * Submission Detail:
 * Runtime: 8 ms, faster than 41.53% of C++ online submissions for Plus One.
 * Memory Usage: 8.6 MB, less than 64.21% of C++ online submissions for Plus One.
 */
