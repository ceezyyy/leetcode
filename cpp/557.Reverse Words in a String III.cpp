/**
 * Source: LeetCode 557. Reverse Words in a String III
 * Author: ceezyyy
 * Date: 04-06-2019
 * Reference: @Grandyang http://www.cnblogs.com/grandyang/p/6703311.html
 */


/*
Easy

Share
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: ¡°Let¡¯s take LeetCode contest¡±
Output: ¡°s¡¯teL ekat edoCteeL tsetnoc¡±
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

*/


#include<iostream>
#include<string>
#include<sstream>
using namespace std;

class Solution {
public:
	string reverseWords(string s) {
		istringstream istr;
		string res = ""; // to print out the result(String Output)
		string t = ""; // temporary string
		istr.str(s);
		// In the string, each word is separated by single space 
		// and there will not be any extra space in the string
		while (istr >> t) {
			reverse(t.begin(), t.end());
			res += t + " ";
		}
		res.pop_back(); // pop the last single space
		return res;
	}
};


/**
 * Submission Detail:
 * Runtime: 28 ms, faster than 48.10% of C++ online submissions for Reverse Words in a String III.
 * Memory Usage: 16.2 MB, less than 17.19% of C++ online submissions for Reverse Words in a String III.
 */
