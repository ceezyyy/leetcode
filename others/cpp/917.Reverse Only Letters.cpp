/**
 * Source: LeetCode 917. Reverse Only Letters
 * Author: ceezyyy
 * Date: 04-07-2019
 * Reference: @Huahua https://zxi.mytechroad.com/blog/string/leetcode-917-reverse-only-letters/
 */


/*
Easy

Share
Given a string S, return the ¡°reversed¡± string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: ¡°ab-cd¡±
Output: ¡°dc-ba¡±

Example 2:
Input: ¡°a-bC-dEf-ghIj¡±
Output: ¡°j-Ih-gfE-dCba¡±

Example 3:
Input: ¡°Test1ng-Leet=code-Q!¡±
Output: ¡°Qedo1ct-eeLg=ntse-T!¡±

Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn¡¯t contain \ or "

*/


#include<iostream>
#include<string>
#include<locale>
using namespace std;

class Solution {
public:
	string reverseOnlyLetters(string S) {
		int i = 0;
		int j = S.size() - 1;
		while (i < j) {
			// int isalpha ( int c );
			// check if character is alphabetic
			if (isalpha(S.at(i)) && isalpha(S.at(j))) {
				swap(S.at(i++), S.at(j--));
			}
			else {
				if (isalpha(S.at(i)) == 0) {
					i++;
				}
				else {
					j--;
				}
			}
		}
		return S;
	}
};


// Study Notes:
// Two Pointer & String
// learn the function <cctype> isalpha
// http://www.cplusplus.com/reference/cctype/isalpha/


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Reverse Only Letters.
 * Memory Usage: 8.3 MB, less than 100.00% of C++ online submissions for Reverse Only Letters.
 */
