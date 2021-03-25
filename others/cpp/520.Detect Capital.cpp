/*
Source: LeetCode 520. Detect Capital
Author: ceezyyy
Date: 03-10-2019
*/


/*

520. Detect Capital

Easy

Share
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like “USA”.
All letters in this word are not capitals, like “leetcode”.
Only the first letter in this word is capital if it has more than one letter, like “Google”.
Otherwise, we define that this word doesn’t use capitals in a right way.

Example 1:
Input: “USA”
Output: True

Example 2:
Input: “FlaG”
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

*/


#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

class Solution {
public:
	bool detectCapitalUse(string word) {
		int countCaseOne = 0;
		int countCaseTwo = 0;
		int countCaseThree = 0;
		/*
		A special situation
		*/
		if (word.size() <= 1) {
			return true;
		}
		/*
		Determine if the first letter is capitalized
		*/
		if (word[0] >= 'A' && word[0] <= 'Z') {
			for (int i = 1; i < word.size(); i++) {
				/*
				Case Three:
				Only the first letter in this word is capital if it has more than one
				letter, like "Google".
				*/
				if (word[i] >= 'a' && word[i] <= 'z') {
					countCaseThree++;
				}
				/*
				Case One: All letters in this word are capitals, like "USA".
				*/
				if (word[i] >= 'A' && word[i] <= 'Z') {
					countCaseOne++;
				}
			}
			if ((countCaseOne == word.size() - 1) || (countCaseThree == word.size() - 1)) {
				return true;
			}
		}
		else {
			for (int i = 0; i < word.size(); i++) {
				/*
				Case Two: All letters in this word are not capitals, like "leetcode".
				*/
				if (word[i] >= 'a' && word[i] <= 'z') {
					countCaseTwo++;
				}
			}
			if (countCaseTwo == word.size()) {
				return true;
			}
		}
		return false;
	}
};

/*
Submission Detail：

Runtime: 8 ms
Memory Usage: 11.4 MB
*/
