/**
 * Source: LeetCode  500. Keyboard Row
 * Author: ceezyyy
 * Date: 04-19-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/6421749.html
 */


/*
Easy

Share
Given a List of words, return the words that can be typed using letters of alphabet on only one row¡¯s of American keyboard like the image below.

Example:
Input: [¡°Hello¡±, ¡°Alaska¡±, ¡°Dad¡±, ¡°Peace¡±]
Output: [¡°Alaska¡±, ¡°Dad¡±]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

*/


#include<iostream>
#include<vector>
#include<set>
using namespace std;

class Solution {
public:
	vector<string> findWords(vector<string>& words) {
		vector<string> res;
		// note: you may assume the input string will only contain letters of alphabet
		set<char> row1 = { 'q','w','e','r','t','y','u','i','o','p' };
		set<char> row2 = { 'a','s','d','f','g','h','j','k','l' };
		set<char> row3 = { 'z','x','c','v','b','n','m' };
		for (string word : words) {
			int r1 = 0, r2 = 0, r3 = 0; // initialize to 0
			for (char c : word) {
				if (c < 'a') { c += 32; } // uppercase -> lowercase
				if (row1.count(c))
					r1 = 1; // char c in row1
				if (row2.count(c))
					r2 = 1;
				if (row3.count(c))
					r3 = 1;
				if (r1 + r2 + r3 > 1) // next word
					break;
			}
			if (r1 + r2 + r3 == 1) {
				// letters of alphabet on only one row's of American keyboard
				res.push_back(word);
			}
		}
		return res;
	}
};


// Study Notes:
// The set::count() is a built-in function in C++ STL which returns the number of times an element occurs in the set. It can only return 1 or 0 as the set container contains unique elements only.
// set_name.count(element) 


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Keyboard Row.
 * Memory Usage: 8.4 MB, less than 100.00% of C++ online submissions for Keyboard Row.
 */
