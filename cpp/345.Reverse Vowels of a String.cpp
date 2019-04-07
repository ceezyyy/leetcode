/**
 * Source: LeetCode 345. Reverse Vowels of a String
 * Author: ceezyyy
 * Date: 04-07-2019
 */


/*
Easy

Share
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: ¡°hello¡±
Output: ¡°holle¡±

Example 2:
Input: ¡°leetcode¡±
Output: ¡°leotcede¡±

Note:
The vowels does not include the letter ¡°y¡±.

*/


#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
	string reverseVowels(string s) {
		int i = 0;
		int j = s.size() - 1;
		while (i < j) {
			if ((s.at(i) == 'a' || s.at(i) == 'A' || s.at(i) == 'e' || s.at(i) == 'E' || s.at(i) == 'i' || s.at(i) == 'I' || s.at(i) == 'o' || s.at(i) == 'O' || s.at(i) == 'u' || s.at(i) == 'U') && (s.at(j) == 'a' || s.at(j) == 'A' || s.at(j) == 'e' || s.at(j) == 'E' || s.at(j) == 'i' || s.at(j) == 'I' || s.at(j) == 'o' || s.at(j) == 'O' || s.at(j) == 'u' || s.at(j) == 'U')) {
				swap(s.at(i++), s.at(j--));
			}
			else {
				if (s.at(i) == 'a' || s.at(i) == 'A' || s.at(i) == 'e' || s.at(i) == 'E' || s.at(i) == 'i' || s.at(i) == 'I' || s.at(i) == 'o' || s.at(i) == 'O' || s.at(i) == 'u' || s.at(i) == 'U') {
					j--;
				}
				else {
					i++;
				}
			}
		}
		return s;
	}
};


/**
 * Submission Detail:
 * Runtime: 12 ms, faster than 98.06% of C++ online submissions for Reverse Vowels of a String.
 * Memory Usage: 9.8 MB, less than 65.24% of C++ online submissions for Reverse Vowels of a String.
 */
