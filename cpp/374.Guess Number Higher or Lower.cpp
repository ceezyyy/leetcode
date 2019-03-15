/*
Source: LeetCode 374. Guess Number Higher or Lower 
Author: ceezyyy
Date: 03-15-2019
*/


/*
Easy

Share
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I¡¯ll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
1 : My number is higher
0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6

*/


#include<iostream>
#include<algorithm>
using namespace std;
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
	int guessNumber(int n) { //A number from 1 to n
		int l = 1;
		int r = n;
		int mid;
		while (l <= r) {
			mid = l + (r - l) / 2;
			if (guess(mid) == 0) {
				return mid;
			}
			else if (guess(mid) > 0) {
				l = mid + 1;
			}
			else {
				r = mid - 1;
			}
		}
		return -1;
	}
};


/*
Submission Detail:

Runtime: 4 ms, faster than 100.00% of C++ online submissions for Guess Number Higher or Lower.
Memory Usage: 8.3 MB, less than 13.43% of C++ online submissions for Guess Number Higher or Lower.

*/
