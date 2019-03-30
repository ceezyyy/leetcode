/*
Source: LeetCode 387. First Unique Character in a String
Author: ceezyyy
Date: 03-30-2019
*/


/*
Easy

Share
Given a string, find the first non-repeating character in it and return it¡¯s index. 
If it doesn¡¯t exist, return -1.

Examples:
s = ¡°leetcode¡±
return 0.

s = ¡°loveleetcode¡±,
return 2.

Note: You may assume the string contain only lowercase letters.

*/


#include<iostream>
#include<string>
#include<map>
using namespace std;

class Solution {
public:
	int firstUniqChar(string s) {
		/*
		Record the number of occurrences of each character
		*/
		map<char, int> occurence;
		for (char c : s) {
			occurence[c]++;
		}
		for (int j = 0; j < s.size(); j++) {
			if (occurence[s.at(j)] == 1) {
				return j;
			}
		}
		return -1;
	}
};


/*
Submission Detail:

Runtime: 76 ms, faster than 28.63% of C++ online submissions for First Unique Character in a String.
Memory Usage: 13 MB, less than 98.32% of C++ online submissions for First Unique Character in a String.

*/
