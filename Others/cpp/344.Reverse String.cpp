/**
 * Source: LeetCode  344. Reverse String
 * Author: ceezyyy
 * Date: 10-02-2019
 */


/*
Easy

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

*/


#include<vector>
using namespace std;

class Solution {
public:
	void reverseString(vector<char>& s) {
		// here is 'i<s.size()/2' instead of 'i<=s.size()/2'
		for (int i = 0, j = s.size() - 1; i < s.size() / 2; i++, j--) {  
			swap(s.at(i), s.at(j));
		}
	}

};


/**
 * Runtime: 48 ms, faster than 74.11% of C++ online submissions for Reverse String.
 * Memory Usage: 15.2 MB, less than 90.24% of C++ online submissions for Reverse String.
 */


/**
 * Study Notes:
 * Test all the examples before you submit the solution.
 */
