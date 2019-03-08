/*
Source: LeetCode 771. Jewels and Stones
Author: ceezyyy
Date: 03-03-2019
*/

/*
Easy

Share
You¡¯re given strings J representing the types of stones that are jewels, and S representing the stones you have. Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so ¡°a¡± is considered a different type of stone from ¡°A¡±.

Example 1:

Input: J = ¡°aA¡±, S = ¡°aAAbbbb¡±
Output: 3
Example 2:

Input: J = ¡°z¡±, S = ¡°ZZ¡±
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.


*/


#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
	int numJewelsInStones(string J, string S) {
		int amount = 0;
		for (int i = 0; i < J.length(); i++) {
			for (int j = 0; j < S.length(); j++) {
				if (J.at(i) == S.at(j)) { //match
					amount++;
				}
			}
		}
		return amount;
	}
};
